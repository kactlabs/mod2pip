# Development Guide for mod2pip

## Quick Setup

```bash
# Clone the repository
git clone https://github.com/kactlabs/mod2pip.git
cd mod2pip

# Install development dependencies
pip install -r requirements-dev.txt

# Install the package in development mode
pip install -e .
```

## Development Workflow

### Running Tests

```bash
# Run tests on current Python version
python -m unittest discover -s tests -p "test_*.py" -v

# Run tests with debug information
make test-all

# Run flake8 linting
flake8 mod2pip tests/test_mod2pip.py --max-line-length=100

# Run debug script to check environment
python ci_debug.py

# Test all new features (v0.7.0)
python test_mod2pip_features.py
```

### Code Quality

```bash
# Check code style
make lint

# Run coverage
make coverage
```

### Building and Publishing

```bash
# Build the package
make build
# or
python -m build

# Check the build
twine check dist/*

# Publish to PyPI
make publish
# or
twine upload dist/*

# Publish to test PyPI
make publish-to-test
# or
twine upload --repository testpypi dist/*
```

## Available Make Commands

```bash
make help                 # Show all available commands
make clean                # Remove all build artifacts
make test                 # Run tests quickly
make test-all             # Run tests on all Python versions
make lint                 # Check code style
make coverage             # Generate coverage report
make build                # Build the package
make install              # Install in development mode
make install-dev          # Install development dependencies
```

## Dependencies

### Runtime Dependencies
- `yarg>=0.1.9` - PyPI package information
- `docopt>=0.6.2` - Command line interface
- `requests>=2.25.0` - HTTP requests for PyPI API
- `nbconvert>=7.11.0` - Jupyter notebook processing
- `ipython>=7.16.0` - IPython integration (version-specific)

### Development Dependencies
- `flake8>=6.1.0` - Code linting
- `coverage>=7.3.2` - Code coverage
- `twine>=4.0.0` - PyPI publishing
- `build>=0.10.0` - Package building

## Python Version Support

mod2pip supports Python 3.9 through 3.13:
- Python 3.9: ipython>=7.16.0,<8.0.0
- Python 3.10-3.12: ipython>=8.0.0,<8.19.0
- Python 3.13: ipython>=8.18.0

## CI/CD

The project uses GitHub Actions for continuous integration:
- Tests run on Python 3.9, 3.10, 3.11, 3.12, 3.13, and PyPy
- Code quality checks with flake8
- Coverage reporting with Codecov

## Project Structure

```
mod2pip/
├── mod2pip/              # Main package
│   ├── __init__.py
│   ├── mod2pip.py        # Core functionality
│   ├── mapping           # Package name mappings
│   └── stdlib            # Standard library modules
├── tests/                # Test suite
├── docs/                 # Documentation
├── test_mod2pip_features.py  # Comprehensive test suite for v0.7.0 features
├── demo_project.py       # Demo file for testing all features
├── requirements-dev.txt  # Development dependencies
├── pyproject.toml        # Package configuration
├── tox.ini              # Tox configuration
└── Makefile             # Development commands
```

## New Features (v0.10.0)

### --lib Flag
Add specific libraries with their installed versions:
```bash
mod2pip --force --lib langchain,langchain-core
```

### --generate-env Flag
Scan Python files for environment variables and generate .env files:
```bash
mod2pip --generate-env --force
```

### Comprehensive Test Suite
Run all feature tests:
```bash
python test_mod2pip_features.py
```

### Demo Project
Run the demo to see all features:
```bash
python demo_project.py
```

See README.md and CHANGELOG.md for detailed usage examples.

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Run tests: `make test-all`
5. Check code quality: `make lint`
6. Submit a pull request

## Troubleshooting

### Python 3.13 Issues
If you encounter issues with Python 3.13:
- Ensure you have the latest versions of dependencies
- Use `pip install --upgrade pip setuptools wheel`
- Check that nbconvert>=7.16.0 and ipython>=8.18.0 are installed

### Tox Issues
If you need to test multiple Python versions:
- Use GitHub Actions CI which tests Python 3.9-3.13
- Or manually test with different Python environments
- Check that all dependencies install correctly: `pip install -r requirements-dev.txt`