from setuptools import setup,find_packages
from os.path import join
import sys


if sys.version_info < (3,):
    print("Python 2 is not supported.\n please try with python>=3.6 ")
    sys.exit(-1)


with open("README.md", "r", encoding="utf-8") as readme:
    long_description=readme.read()


with open(join("antargyan", "version.py")) as set_version:
    exec(set_version.read())


setup(
    name="antargyan",
    version=__version__,
    author="vinay patil",
    author_email="mailforguglecolabco.in@gmail.com",
    description="All ml/dl algorithms implemnted in numpy/tensorflow/pytorch",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Vinaypatil-Ev/vinEvPy-antarjnan",
    project_urls={
        'Source Code': 'https://github.com/Vinaypatil-Ev/vinEvPy-antarjnan',
        },
    install_requires=[
        'numpy',
        'torch>=1.5.0',
    ],
    packages=find_packages()
    python_requires='>=3.6.1',
    classifiers=[
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        "License :: OSI Approved :: MIT License",
        'Intended Audience :: Science/Research',
        'Intended Audience :: Education',
        "Topic :: Scientific/Engineering",
        "Topic :: Scientific/Engineering :: Mathematics",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
    ],
    license='MIT',
    keywords='antargyan vinaypatil-ev vinevpy machine learning tensorflow pytorch numpy algorithms machinelearnig ' 
)