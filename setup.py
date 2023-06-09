from setuptools import setup, find_packages
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

VERSION = '0.0.1'
DESCRIPTION = 'Tri-Model Ensemble System for Classification'

# Setting up
setup(
    name="TriModelSystem",
    version=VERSION,
    author="Arkitech (Joshua Tan)",
    author_email="<joshuatan.helios@gmail.com>",
    description=DESCRIPTION,
    packages=find_packages(),
    install_requires=['tensorflow'],
    keywords=['python', 'machine learning', 'tensorflow', 'classification', 'neural network'],
    classifiers=[
        "Development Status :: 1 - Development",
        "Intended Audience :: Researches",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)
