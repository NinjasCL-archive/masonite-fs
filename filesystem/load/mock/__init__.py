# coding: utf-8

from fs.copy import copy_fs, copy_structure

from filesystem import load

# See https://docs.pyfilesystem.org/en/latest/reference/copy.html?highlight=copy_structure#fs.copy.copy_fs


def root(walker=None):

    base = load.root()
    mock = load.mock()

    copy_fs(base, mock, walker=walker)
    base.close()

    return mock


def root_only_structure(walker=None):

    base = load.root()
    mock = load.mock()

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
    return load.app(___get_fat_or_slim_fs(slim))


def bootstrap(slim=False):
    return load.bootstrap(___get_fat_or_slim_fs(slim))


def config(slim=False):
    return load.config(___get_fat_or_slim_fs(slim))


def databases(slim=False):
    return load.databases(___get_fat_or_slim_fs(slim))


def resources(slim=False):
    return load.resources(___get_fat_or_slim_fs(slim))


def routes(slim=False):
    return load.routes(___get_fat_or_slim_fs(slim))


def storage(slim=False):
    return load.storage(___get_fat_or_slim_fs(slim))


def tests(slim=False):
    return load.tests(___get_fat_or_slim_fs(slim))
