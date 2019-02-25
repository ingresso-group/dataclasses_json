import os
from setuptools import setup

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='dataclasses_json',
    version='0.0.1',
    packages=['dataclasses_json'],
    include_package_data=True,
    description=(
        "This module allows for easy conversion to and from JSON",
        "format for common python3 dataclasses"
    ),
    long_description=open('README.md').read(),
    author='Ingresso',
    author_email='systems@ingresso.co.uk',
    install_requires=[
        'python-dateutil==2.7.5',
        'marshmallow==2.18.1'
    ],
)
