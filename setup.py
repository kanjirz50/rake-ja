from setuptools import setup, find_packages
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, "README.md"), encoding="utf-8") as f:
    long_description = f.read()

    setup(
        name="rake-ja",
        version="0.0.1",
        description="",
        long_description=long_description,
        license="MIT",
        packages=find_packages(exclude=["contrib", "docs", "tests"]),
        install_requires=[
            "mecab-python3>=0.7",
            "rake-nltk>=1.0.4"
        ],
        dependency_links=[],
        python_requires='~=3.3',
    )
