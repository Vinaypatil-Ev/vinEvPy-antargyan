from setuptools import setup
from os.path import join
import sys


if sys.version_info < (3,):
    print("Python 2 is not supported.\n please try with python>=3.6 ")
    sys.exit(-1)


with open("README.md", "r") as readme:
    long_description=readme.read()


with open(join("antargyan", "version.py")) as set_version:
    exec(set_version.read())


setup(
    name="antargyan",
    auther="vinay patil",
    auther_email="mailforguglecolabco.in@gmail.com",
    version=__version__,
    long_description=long_description,
    url="https://github.com/Vinaypatil-Ev/vinEvPy-antarjnan",
    install_requires=[
        'numpy',
        'torch>=1.5.0',
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Topic :: Scientific/Engineering",
        "Topic :: Scientific/Engineering :: Mathematics",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
    ],
    license='MIT',
    keywords='antargyan vinaypatil-ev vinevpy machine learning tensorflow pytorch numpy algorithms machinelearnig ' 
)