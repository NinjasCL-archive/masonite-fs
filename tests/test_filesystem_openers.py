# coding: utf-8

from the import expect

from filesystem import openers


class TestFileSystemOpeners:

    def setup_method(self):
        pass

    def test_that_opener_os_exists(self):
        expect(openers.OPERATING_SYSTEM).to.be.NOT.empty

    def test_that_opener_os_is_correct(self):
        expect(openers.OPERATING_SYSTEM).to.be.eq('osfs://')

    def test_that_opener_mem_exists(self):
        expect(openers.MEMORY).to.be.NOT.empty

    def test_that_opener_mem_is_correct(self):
        expect(openers.MEMORY).to.be.eq('mem://')
