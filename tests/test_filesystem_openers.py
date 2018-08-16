# coding: utf-8

from the import expect

from filesystem import Openers


class TestFileSystemOpeners:

    def setup_method(self):
        pass

    def test_that_opener_os_exists(self):
        expect(Openers.OPERATING_SYSTEM).to.be.NOT.empty

    def test_that_opener_os_is_correct(self):
        expect(Openers.OPERATING_SYSTEM).to.be.eq('osfs://')

    def test_that_opener_mem_exists(self):
        expect(Openers.MEMORY).to.be.NOT.empty

    def test_that_opener_mem_is_correct(self):
        expect(Openers.MEMORY).to.be.eq('mem://')
