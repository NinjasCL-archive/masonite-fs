# coding: utf-8

from fs.copy import copy_fs, copy_structure

from filesystem import Open

# See https://docs.pyfilesystem.org/en/latest/reference/copy.html?highlight=copy_structure#fs.copy.copy_fs


def root(walker=None):

    base = Open.root()
    mock = Open.mock()

    copy_fs(base, mock, walker=walker)
    base.close()

    return mock


def root_only_structure(walker=None):

    base = Open.root()
    mock = Open.mock()

    copy_structure(base, mock, walker=walker)
    base.close()

    return mock


def ___get_fat_or_slim_fs(slim=False):

    if slim:
        _fs = root_only_structure()
    else:
        _fs = root()

    return _fs


def app(slim=False):
    return Open.app(___get_fat_or_slim_fs(slim))


def bootstrap(slim=False):
    return Open.bootstrap(___get_fat_or_slim_fs(slim))


def config(slim=False):
    return Open.config(___get_fat_or_slim_fs(slim))


def databases(slim=False):
    return Open.databases(___get_fat_or_slim_fs(slim))


def resources(slim=False):
    return Open.resources(___get_fat_or_slim_fs(slim))


def routes(slim=False):
    return Open.routes(___get_fat_or_slim_fs(slim))


def storage(slim=False):
    return Open.storage(___get_fat_or_slim_fs(slim))


def tests(slim=False):
    return Open.tests(___get_fat_or_slim_fs(slim))
