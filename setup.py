# -*- coding: utf-8 -*-
# flake8-chart - flake8 stats visualised
# Copyright (C) 2015  james sangho nah <sangho.nah@gmail.com>

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

import flake8chart


setup(
    name="flake8-chart",
    version=flake8chart.__version__,
    author=flake8chart.__author__,
    author_email=flake8chart.__email__,
    description="flake8 stats visualised",
    long_description=open("README.rst").read(),
    license="MIT License",
    url="https://github.com/microamp/flake8-chart",
    py_modules=["flake8chart"],
    classifiers=(
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.4",
        "Topic :: Software Development :: Quality Assurance"
    ),
    entry_points={"console_scripts": ["flake8chart = flake8chart:flake8chart"]}
)
