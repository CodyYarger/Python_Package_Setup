#!/usr/bin/env python3
# 01/29/2021
# Dev: Cody Yarger
# Exercise 6 - Mailroom Package
""" Setup script to install mailroom package. """

from setuptools import setup

setup(
    # Setup arguments for mailroom package installation
    name='mailroom',
    author='Cody Yarger',
    version='0.1.0',
    packages=['mailroom', 'mailroom/tools'],
    description='Manages donors and dontations database',
    test_suite="test.test_mailroom",
    include_package_data=True,
    package_data={'mailroom': ['*.csv']},
    entry_points={
        'console_scripts': ['mailroom=mailroom.mailroom:main'],
    },
    install_requires=[
        "pytest"
    ],
)


# ===============================================================================
#     # the good to have stuff: particularly if you are distributing it
#     url='http://pypi.python.org/pypi/PackageName/',
#     license='LICENSE.txt',
#     description='An awesome package that does something',
#     long_description=open('README.txt').read(),
# )
