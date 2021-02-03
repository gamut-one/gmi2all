#!/usr/bin/env python

import setuptools
import codecs
import os.path

def read(rel_path):
    here = os.path.abspath(os.path.dirname(__file__))
    with codecs.open(os.path.join(here, rel_path), 'r') as fp:
        return fp.read()


def get_version(rel_path):
    for line in read(rel_path).splitlines():
        if line.startswith('__version__'):
            delim = '"' if '"' in line else "'"
            return line.split(delim)[1]
    else:
        raise RuntimeError("Unable to find version string.")


with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="gmi2all",  # Replace with your own username
    version=get_version('gmi2all.py'),
    author="Andrew Williams",
    author_email="andy@tensixtyone.com",
    description="Gemini document converter",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/gamut-one/gmi2all",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    py_modules=['gmi2all'],
    entry_points={
        'console_scripts': ['gmi2all=gmi2all:main'],
    }
)

