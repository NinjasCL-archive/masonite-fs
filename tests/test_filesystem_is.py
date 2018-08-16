# coding: utf-8
import os

from the import expect

from filesystem import Is


class TestFilesystemIs:

    def setup_method(self):
        self.path = os.path.dirname(os.path.realpath(__file__))

    def test_that_is_directory_works_with_dir(self):
        result = Is.directory(self.path + '/files')
        expect(result).to.be(True)

    def test_that_is_directory_do_not_works_with_file(self):
        result = Is.directory(self.path + '/files/not-empty-dir/not-empty-file')
        expect(result).to.be(False)
