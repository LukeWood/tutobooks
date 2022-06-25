# Copyright 2019 The KerasCV Authors
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Setup script."""

import pathlib

from setuptools import find_packages
from setuptools import setup

HERE = pathlib.Path(__file__).parent
README = (HERE / "README.md").read_text()

description = """
A simple package to convert between tutobooks python files, jupyter notebooks and
markdown."""

setup(
    name="tutobooks",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/lukewood/tutobooks",
    author="Keras team",
    description=description,
    author_email="lukewoodcs@gmail.com",
    license="Apache License 2.0",
    install_requires=["packaging", "absl-py"],
    extras_require={
        "tests": ["flake8", "isort", "black", "pytest"],
    },
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.7",
        "Operating System :: Unix",
        "Operating System :: Microsoft :: Windows",
        "Operating System :: MacOS",
        "Topic :: Scientific/Engineering",
        "Topic :: Software Development",
    ],
    include_package_data=True,
    entry_points={
        'console_scripts': [
            'tutobooks = tutobooks.tutobooks:main',
        ],
    },
    packages=find_packages(exclude=("*_test.py",)),
)
