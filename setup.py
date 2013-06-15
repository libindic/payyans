#!/usr/bin/env python

from setuptools import setup,find_packages

name = 'payyans'

setup(
    name = name,
    version = "0.1",
    url = "http://silpa.org.in/payyans",
    license = "LGPL 3.0",
    description = "ASCII to Unicode converter",
    author = 'Santhosh Thottingal',
    author_email = "santhosh.thottingal@gmail.com",
    long_description = """This library helps to convert
ascii texts to unicode.""",
    packages=find_packages(),
    include_package_data = True,
    setup_requires = ['setuptools-git'],
    install_requires = ['setuptools', 'normalizer'],
    zip_safe = False,
    )
