.PHONY: clean-pyc clean-build docs clean help

help:
	@echo "clean - remove all build, test, coverage and Python artifacts"
	@echo "clean-build - remove build artifacts"
	@echo "clean-pyc - remove Python file artifacts"
	@echo "clean-test - remove test and coverage artifacts"
	@echo "lint - check style with flake8"
	@echo "test - run tests quickly using the default Python"
	@echo "test-all - run tests on every Python version with tox"
	@echo "coverage - check code coverage quickly with the default Python"
	@echo "docs - generate Sphinx HTML documentation, including API docs"
	@echo "publish - package and upload a release"
	@echo "publish-to-test - package and upload a release to test-pypi"
	@echo "build - build the package"
	@echo "install - install the package in development mode"
	@echo "install-dev - install development dependencies"

clean: clean-build clean-pyc clean-test

clean-build:
	rm -fr build/
	rm -fr dist/
	rm -fr .eggs/
	find . -name '*.egg-info' -exec rm -fr {} +
	find . -name '*.egg' -exec rm -rf {} +

clean-pyc:
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +
	find . -name '__pycache__' -exec rm -fr {} +

clean-test:
	rm -fr .tox/
	rm -f .coverage
	rm -fr htmlcov/

lint:
	flake8 mod2pip tests

test:
	python -m unittest discover 

test-all:
	tox

coverage:
	coverage run --source mod2pip -m unittest discover
	coverage report -m
	coverage html
	open htmlcov/index.html

docs:
	rm -f docs/mod2pip.rst
	rm -f docs/modules.rst
	sphinx-apidoc -o docs/ mod2pip
	$(MAKE) -C docs clean
	$(MAKE) -C docs html
	open docs/_build/html/index.html

publish: build
	twine upload dist/*

publish-to-test: build
	twine upload --repository testpypi dist/*

build: clean
	python -m build

install: clean
	pip install -e .

install-dev:
	pip install -r requirements-dev.txt
	pip install -e .