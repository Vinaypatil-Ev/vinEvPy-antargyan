from setuptools import setup
from os.path import join

if sys.version_info < (3,):
    print("Python 2 is not supported.\n please try with python>=3.6 ")
    sys.exit(-1)
    
with open("README.md","r") as readme:
    long_description=readme.read()
    
    
with open(join("antarjnan","version.py")) as set_version:
    exec(set_version.read())

setup(
    name="antarjyan",
    auther="vinay patil",
    auther_email="mailforguglecolabco.in@gmail.com",
    version=__version__,
    long_description=long_description,
    url="https://github.com/Vinaypatil-Ev/vinEvPy-antarjnan.git",
    install_requires=[
        'matplotlib==3.3.1',
        'numpy',
        'pandas',
        'seaborn==0.8.1',
        'tensorflow>=1.10.0,<2.0',
        'torch==1.5.0',
        'tqdm'
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Window tested",
        "Topic :: Scientific/Engineering",
        "Topic :: Scientific/Engineering :: Mathematics",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
    ],
    license='MIT',
    keywords='vinaypatil-ev vinevpy antarjnan machine learning'
    
)