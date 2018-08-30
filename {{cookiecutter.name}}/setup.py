#!/usr/bin/env python

import setuptools  # type: ignore

setuptools.setup(
    name="{{cookiecutter.name}}",
    version="0.0.1",
    license="EUPL-1.2",
    author="{{cookiecutter.author}}",
    author_email="{{cookiecutter.email}}",
    url="{{cookiecutter.url}}",
    description="{{cookiecutter.description}}",
    long_description_content_type="text/markdown",
    long_description=open("README.md", "r").read(),
    keywords="{{cookiecutter.keywords}}",
    classifiers=[
        "Environment :: Console",
        "Operating System :: POSIX",
        "Natural Language :: English",
        "Development Status :: 3 - Alpha",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: European Union Public Licence 1.2 (EUPL 1.2)",
    ],
    extras_require={
        "dist": ["pip", "twine", "wheel", "setuptools"],
        "repl": ["jedi", "ptpdb", "ipython", "ptpython"],
        "test": ["pytest", "pytest-mypy", "pytest-black", "pytest-flakes"],
    },
    python_requires=">={{cookiecutter.python}}",
    install_requires=[],
    packages=setuptools.find_packages(),
    entry_points={
        "console_scripts": ["{{cookiecutter.name}}={{cookiecutter.name}}:main"]
    },
)
