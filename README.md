# mod2pip - Generate requirements.txt file for any project based on imports

[![Tests](https://github.com/kactlabs/mod2pip/actions/workflows/tests.yml/badge.svg)](https://github.com/kactlabs/mod2pip/actions/workflows/tests.yml)
[![PyPI version](https://img.shields.io/pypi/v/mod2pip.svg)](https://pypi.python.org/pypi/mod2pip)
[![codecov](https://codecov.io/gh/kactlabs/mod2pip/branch/master/graph/badge.svg?token=0rfPfUZEAX)](https://codecov.io/gh/kactlabs/mod2pip)
[![License](https://img.shields.io/pypi/l/mod2pip.svg)](https://pypi.python.org/pypi/mod2pip)

## About This Fork

This repository is forked from [mod2pip - https://github.com/kactlabs/mod2pip](https://github.com/kactlabs/mod2pip) with additional bugfixes and improvements.

## Installation

```sh
pip install mod2pip
```

**Note:** If you don't want support for jupyter notebooks, you can install mod2pip without the dependencies that give support to it:

```sh
pip install --no-deps mod2pip
pip install yarg==0.1.9 docopt==0.6.2
```

## Usage

```
Usage:
    mod2pip [options] [<path>]

Arguments:
    <path>                The path to the directory containing the application files for which a requirements file
                          should be generated (defaults to the current working directory)

Options:
    --use-local           Use ONLY local package info instead of querying PyPI
    --pypi-server <url>   Use custom PyPi server
    --proxy <url>         Use Proxy, parameter will be passed to requests library. You can also just set the
                          environments parameter in your terminal:
                          $ export HTTP_PROXY="http://10.10.1.10:3128"
                          $ export HTTPS_PROXY="https://10.10.1.10:1080"
    --debug               Print debug information
    --ignore <dirs>...    Ignore extra directories, each separated by a comma
    --no-follow-links     Do not follow symbolic links in the project
    --encoding <charset>  Use encoding parameter for file open
    --savepath <file>     Save the list of requirements in the given file
    --print               Output the list of requirements in the standard output
    --force               Overwrite existing requirements.txt
    --diff <file>         Compare modules in requirements.txt to project imports
    --clean <file>        Clean up requirements.txt by removing modules that are not imported in project
    --mode <scheme>       Enables dynamic versioning with <compat>, <gt> or <non-pin> schemes
                          <compat> | e.g. Flask~=1.1.2
                          <gt>     | e.g. Flask>=1.1.2
                          <no-pin> | e.g. Flask
    --scan-notebooks      Look for imports in jupyter notebook files.
```

## Example

```sh
$ mod2pip /home/project/location
Successfully saved requirements file in /home/project/location/requirements.txt
```

Contents of requirements.txt:

```
wheel==0.23.0
Yarg==0.1.9
docopt==0.6.2
```

## Why not pip freeze?

- `pip freeze` only saves the packages that are installed with `pip install` in your environment.
- `pip freeze` saves all packages in the environment including those that you don't use in your current project (if you don't have `virtualenv`).
- Sometimes you just need to create `requirements.txt` for a new project without installing modules.