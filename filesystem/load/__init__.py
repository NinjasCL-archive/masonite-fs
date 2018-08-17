# coding: utf-8

from fs import open_fs

from filesystem import openers, paths


def os(path='.'):
    # We will use the current dir in the operating system fs as default value
    return open_fs(openers.OPERATING_SYSTEM + path)


def mock():
    return open_fs(openers.MEMORY)


def fs(opener):
    return open_fs(opener)


# load Masonite Directories

def root():
    return os(paths.ROOT)


def ___open_dir(path, base=None):

    if base is None:
        base = root()

    _fs = base.opendir(path)
    base.close()

    return _fs


def app(base=None):
    return ___open_dir(paths.APP, base)


def bootstrap(base=None):
    return ___open_dir(paths.BOOTSTRAP, base)


def config(base=None):
    return ___open_dir(paths.CONFIG, base)


def databases(base=None):
    return ___open_dir(paths.DATABASES, base)


def resources(base=None):
    return ___open_dir(paths.RESOURCES, base)


def routes(base=None):
    return ___open_dir(paths.ROUTES, base)


def storage(base=None):
    return ___open_dir(paths.STORAGE, base)


def tests(base=None):
    return ___open_dir(paths.TESTS, base)
