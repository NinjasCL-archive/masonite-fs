# coding: utf-8

from the import expect

from filesystem import load, paths


class TestFileSystemHelpers:

    def setup_method(self):
        pass

    def test_that_os_return_fs(self):

        info = load.os().getinfo('.')

        expect(info).to.be.NOT.empty

    def test_that_mock_return_fs(self):

        info = load.mock().getinfo('.')

        expect(info).to.be.NOT.empty

    def test_that_fs_return_fs(self):

        info = load.fs('mem://').getinfo('.')

        expect(info).to.be.NOT.empty

    def test_that_root_return_fs(self):

        info = load.root().getinfo('.')

        expect(info).to.be.NOT.empty

    def test_that_root_is_correct(self):

        info = load.root().getsyspath('.')

        expect(info).to.match(paths.ROOT + '/.')
