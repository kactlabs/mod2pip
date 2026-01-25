#!/bin/bash
# Publish script for mod2pip to PyPI

set -e  # Exit on error

echo "🚀 Publishing mod2pip to PyPI"
echo "================================"

# Check if build and twine are installed
if ! command -v python -m build &> /dev/null; then
    echo "❌ 'build' not found. Installing..."
    pip install --upgrade build
fi

if ! command -v twine &> /dev/null; then
    echo "❌ 'twine' not found. Installing..."
    pip install --upgrade twine
fi

# Clean previous builds
echo ""
echo "🧹 Cleaning previous builds..."
rm -rf dist/ build/ *.egg-info mod2pip.egg-info

# Build the package
echo ""
echo "📦 Building package..."
python -m build

# Check the package
echo ""
echo "✅ Checking package..."
twine check dist/*

# Show what will be uploaded
echo ""
echo "📋 Files to upload:"
ls -lh dist/

# Ask for confirmation
echo ""
read -p "🤔 Upload to PyPI? (y/n) " -n 1 -r
echo
if [[ $REPLY =~ ^[Yy]$ ]]
then
    echo ""
    echo "📤 Uploading to PyPI..."
    twine upload dist/*
    
    echo ""
    echo "✅ Successfully published to PyPI!"
    echo "🔗 View at: https://pypi.org/project/mod2pip/"
    echo ""
    echo "Test installation with:"
    echo "  pip install --upgrade mod2pip"
else
    echo ""
    echo "❌ Upload cancelled"
    echo ""
    echo "To upload to TestPyPI instead:"
    echo "  twine upload --repository testpypi dist/*"
fi
