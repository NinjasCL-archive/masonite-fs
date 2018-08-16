# coding: utf-8

from fs import open_fs

from filesystem import Openers, Paths


def os(path='.'):
    # We will use the current dir in the operating system fs as default value
    return open_fs(Openers.OPERATING_SYSTEM + path)


def mock():
    return open_fs(Openers.MEMORY)


def fs(opener):
    return open_fs(opener)


# Open Masonite Directories

def root():
    return os(Paths.ROOT)


def ___open_dir(path, base=None):

    if base is None:
        base = root()

    _fs = base.opendir(path)
    base.close()

    return _fs


def app(base=None):
    return ___open_dir(Paths.APP, base)


def bootstrap(base=None):
    return ___open_dir(Paths.BOOTSTRAP, base)


def config(base=None):
    return ___open_dir(Paths.CONFIG, base)


def databases(base=None):
    return ___open_dir(Paths.DATABASES, base)


def resources(base=None):
    return ___open_dir(Paths.RESOURCES, base)


def routes(base=None):
    return ___open_dir(Paths.ROUTES, base)


def storage(base=None):
    return ___open_dir(Paths.STORAGE, base)


def tests(base=None):
    return ___open_dir(Paths.TESTS, base)
