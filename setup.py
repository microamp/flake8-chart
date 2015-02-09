# -*- coding: utf-8 -*-
# flake8-chart - flake8 stats visualised
# Copyright (C) 2015  james sangho nah <sangho.nah@gmail.com>

from setuptools import setup

setup(
    name="flake8-chart",
    description="flake8 stats visualised",
    long_description=open("README.rst").read(),
    version="0.1.2",
    author="james sangho nah",
    author_email="sangho.nah@gmail.com",
    license="MIT License",
    url="https://github.com/microamp/flake8-chart",
    install_requires=["click>=3.3",
                      "pygal>=1.6.2"],
    py_modules=["flake8chart"],
    package_data={"": ["README.rst", "LICENSE"]},
    include_package_data=True,
    zip_safe=False,
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
