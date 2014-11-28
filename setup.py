# -*- coding: utf-8 -*-

from setuptools import setup


setup(
    name='thorium_htmlpurifier',
    description='HTML Purifier validation for Thorium',
    packages=['thorium_htmlpurifier'],
    install_requires=[
        'thorium',
        'html-purifier3>=2.1.0',
    ],
    test_suite='nose.collector',
)
