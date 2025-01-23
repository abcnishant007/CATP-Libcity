import os
from setuptools import setup

# Utility function to read the README file.
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

# define reqs
REQS = [
    "numpy==1.19.4",
    "torch==1.7.1",
    "scipy==1.5.3",
    "pandas==1.1.5",
    "tensorboard==2.4.1",
    "flake8==3.3.0",
    "pep8-naming==0.4.1",
    "scikit-learn==0.24.0",
    "pytest==3.2.1",
    "ray[tune]==1.2.0",
    "tabulate==0.8.9",
    "hyperopt==0.2.5",
    "tqdm==4.60.0",
    "geopy==2.0.0",
    "dgl==0.6.1",
    "fastdtw==0.3.4",
    "networkx==2.5.1",
    "gensim==4.0.1",
    "torchtext==0.6.0",
    "nltk==3.2.4",
    "statsmodels==0.11.0",
    "tensorboardx==2.2",
    "aioredis==1.3.1",
    "aiohttp==3.7.4",
    "idna==2.10",
    "torchdiffeq==0.2.3"
]

setup(
    name = "libcity",
    version = "0.0.5",

    author = "Nish",
    author_email = "xx.xx@gmail.com",
    description = ("agyhsgvdyiuabv."),
    license = "BSD-3",
    keywords = "Eyetracking classification",
    url = "https://github.com/DiGyt/cateyes",
    packages = ["cateyes"],
    include_package_data=True,
    long_description=read('README.md'),
    long_description_content_type='text/markdown',
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: Utilities",
        "License :: OSI Approved :: BSD License",
    ],
    install_requires=REQS,
)
