#!/usr/bin/env python
"""
Test script to verify enhanced mod2pip functionality.
"""

from mod2pip import mod2pip
import os
import sys
import tempfile
import shutil

# Add the current directory to Python path to import mod2pip
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))


def create_test_project():
    """Create a test project with various import patterns."""
    test_dir = tempfile.mkdtemp()

    # Create main.py with static imports
    with open(os.path.join(test_dir, "main.py"), "w") as f:
        f.write("""
import requests
import numpy as np
from flask import Flask
from datetime import datetime
""")

    # Create dynamic_imports.py with dynamic imports
    with open(os.path.join(test_dir, "dynamic_imports.py"), "w") as f:
        f.write("""
import importlib

# Dynamic imports
module_name = "pandas"
pd = importlib.import_module(module_name)

# Conditional import
try:
    import tensorflow as tf
except ImportError:
    tf = None

# Late import in function
def process_data():
    import scipy.stats as stats
    return stats.norm()

# __import__ usage
json_module = __import__('json')
""")

    # Create requirements.txt for comparison
    with open(os.path.join(test_dir, "requirements.txt"), "w") as f:
        f.write("""
requests==2.28.0
numpy==1.21.0
""")

    return test_dir


def test_enhanced_detection():
    """Test enhanced import detection."""
    test_dir = create_test_project()

    try:
        print("Testing enhanced import detection...")

        # Test basic import detection
        imports = mod2pip.get_all_imports(test_dir)
        print(f"Found imports: {imports}")

        # Test local package detection
        local_packages = mod2pip.get_locally_installed_packages()
        print(f"Found {len(local_packages)} local packages")

        # Test package name mapping
        pkg_names = mod2pip.get_pkg_names(imports)
        print(f"Mapped package names: {pkg_names}")

        # Test local import resolution
        local_imports = mod2pip.get_import_local(imports)
        print(f"Resolved local imports: {[pkg['name'] for pkg in local_imports]}")

        print("Enhanced detection test completed successfully!")

    except Exception as e:
        print(f"Test failed: {e}")
        import traceback
        traceback.print_exc()

    finally:
        shutil.rmtree(test_dir)


def test_conda_detection():
    """Test conda environment detection."""
    print("Testing conda environment detection...")

    # Check if we're in a conda environment
    conda_prefix = os.environ.get("CONDA_PREFIX")
    if conda_prefix:
        print(f"Conda environment detected: {conda_prefix}")

        # Test conda package detection
        packages = mod2pip._get_conda_packages()
        print(f"Found {len(packages)} conda packages")

        if packages:
            print("Sample conda packages:")
            for pkg in packages[:5]:  # Show first 5
                print(f"  - {pkg['name']}: {pkg['exports']}")
    else:
        print("No conda environment detected")


def test_transitive_dependencies():
    """Test transitive dependency resolution."""
    print("Testing transitive dependency resolution...")

    # Create sample packages
    sample_packages = [
        {"name": "requests", "version": "2.28.0"},
        {"name": "flask", "version": "2.0.0"}
    ]

    try:
        transitive_deps = mod2pip.get_transitive_dependencies(sample_packages, max_depth=1)
        print(f"Found {len(transitive_deps)} transitive dependencies")

        if transitive_deps:
            print("Transitive dependencies:")
            for dep in transitive_deps:
                print(f"  - {dep['name']}: {dep['version']}")

    except Exception as e:
        print(f"Transitive dependency test failed: {e}")


if __name__ == "__main__":
    print("Running enhanced mod2pip tests...\n")

    test_enhanced_detection()
    print()

    test_conda_detection()
    print()

    test_transitive_dependencies()
    print()

    print("All tests completed!")
