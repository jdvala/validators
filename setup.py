# -*- coding: utf-8 -*-
"""
validators
----------

Python Data Validation for Humans™.
"""

import os
import sys

from setuptools import find_packages, setup

PY3 = sys.version_info[0] == 3
HERE = os.path.dirname(os.path.abspath(__file__))


def get_version():
    filename = os.path.join(HERE, 'validators', '__init__.py')
    with open(filename) as f:
        contents = f.read()
    pattern = r"^__version__ = '(.*?)'$"
    return re.search(pattern, contents, re.MULTILINE).group(1)

extras_require = {
    'test': ['pytest>=2.2.3', 'flake8>=2.4.0', 'isort>=4.2.2', 'pre-commit',],
}

install_requires = [
    'six>=1.4.0',
    'decorator>=3.4.0',
]

setup(
    name='validators',
    version=get_version(),
    url='https://github.com/kvesteri/validators',
    license='MIT',
    author='Konsta Vesterinen',
    author_email='konsta@fastmonkeys.com',
    description='Python Data Validation for Humans™.',
    long_description=__doc__,
    packages=find_packages('.', exclude=['tests', 'tests.*']),
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    install_requires=install_requires,
    build_requires=install_requires,
    extras_require=extras_require,
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    python_requires='>=3.4',
)
