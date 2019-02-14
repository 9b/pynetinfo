#!/usr/bin/env python
import os
from setuptools import setup, find_packages


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name='netinfo',
    version='0.0.1',
    description='Client to interact with Netinfo services.',
    author="Brandon Dixon",
    author_email="brandon@backscatter.io",
    license="MIT",
    packages=find_packages(),
    install_requires=['requests'],
    long_description=read('README.rst'),
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries',
        'Topic :: Security'
    ],
    entry_points={
        'console_scripts': [
            'netinfo = netinfo.cli.client:main'
        ]
    },
    zip_safe=False,
    keywords=['internet scanning', 'cybersecurity', 'defense', 'intelligence']
)
