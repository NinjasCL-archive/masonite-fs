# coding: utf-8
import os

from fs import open_fs

package_directory = os.path.dirname(os.path.realpath(__file__))
version = '0.0.1'


def ___get_fs_for_path(path='.', filesystem=None):

    if filesystem is None:
        filesystem = open_fs(path)
    _fs = filesystem

    return _fs
