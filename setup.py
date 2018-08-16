#!/usr/bin/env python3
# coding: utf-8

from setuptools import find_packages, setup

from filesystem import version


setup(
    name='masonite-fs',
    version=version,
    packages=find_packages(),
    license='MIT',
    author='Camilo Castro',
    author_email='camilo@ninjas.cl',
    description='Provides helper filesystem functions to Masonite',
    url='https://github.com/NinjasCL-labs/masonite-fs',
    install_requires=[
        'masonite',
        'fs',
        'scandir'
    ],
    keywords=['filesystem', 'python3', 'masonite'],
    include_package_data=True,
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ),
)
