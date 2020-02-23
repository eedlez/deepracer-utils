#!/usr/bin/env python3

from setuptools import setup, find_packages
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='deepracer-utils',
    version='0.0.1',
    packages=find_packages(include=["deepracer.*"]),
    description='A set of tools for working with DeepRacer training',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/aws-deepracer-community/deepracer-utils/',
    author='AWS DeepRacer Community',
    classifiers=[
        'Development Status :: 3 - Alpha',

        # Pick your license as you wish
        'License :: OSI Approved :: Apache Software License',

        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',

        'Topic :: Internet :: Log Analysis'
    ],
    keywords='aws deepracer awsdeepracer',
    python_requires='>=3.5.*, <4',
    install_requires=[
        'boto3>=1.12.0',
        'python-dateutil<3.0.0,>=2.1',
        'numpy>=1.18.0',
        'shapely>=1.7.0',
        'matplotlib>=3.1.0'
    ],
    extras_require={
        'dev': ['check-manifest'],
        'test': ['coverage'],
    },
    project_urls={
        'Bug Reports': 'https://github.com/aws-deepracer-community/deepracer-utils/issues',
        'Source': 'https://github.com/aws-deepracer-community/deepracer-utils/',
    },
)