# coding: utf-8
import os
from filesystem import ___get_fs_for_path


def alive(path='.', filesystem=None):

    _fs = ___get_fs_for_path(path, filesystem)

    result = _fs.exists(path)

    _fs.close()

    return result


def directory(path='.', filesystem=None):

    _fs = ___get_fs_for_path(path, filesystem)
    result = os.path.isdir(_fs.getsyspath('.'))

    _fs.close()

    return result


def file(path='.', filesystem=None):

    _fs = ___get_fs_for_path(path, filesystem)
    result = False

    if _fs.exists(path):
        result = os.path.isfile(_fs.getsyspath('.'))

    _fs.close()

    return result


def empty(path='.', filesystem=None):

    _fs = ___get_fs_for_path(path, filesystem)

    result = True

    if directory(_fs):
        result = _fs.isempty('.')

    elif file(_fs):
        content = _fs.gettext()
        result = (content == '')

    _fs.close()

    return result
