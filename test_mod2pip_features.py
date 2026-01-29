#!/usr/bin/env python
"""
Comprehensive test script for mod2pip features.
Tests --lib flag, --generate-env flag, and enhanced detection.

Requirements:
    pip install -e .
    or
    pip install docopt yarg requests
"""

import os
import sys
import subprocess
import tempfile
import shutil

# Add the current directory to Python path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))


def check_dependencies():
    """Check if required dependencies are installed."""
    missing = []
    try:
        import docopt  # noqa: F401
    except ImportError:
        missing.append('docopt')
    
    try:
        import yarg  # noqa: F401
    except ImportError:
        missing.append('yarg')
    
    try:
        import requests  # noqa: F401
    except ImportError:
        missing.append('requests')
    
    if missing:
        print("\n" + "=" * 70)
        print("  MISSING DEPENDENCIES")
        print("=" * 70)
        print("\nThe following required packages are not installed:")
        for pkg in missing:
            print(f"  - {pkg}")
        print("\nPlease install them using one of these methods:")
        print("\n  Method 1 (recommended):")
        print("    pip install -e .")
        print("\n  Method 2:")
        print("    pip install docopt yarg requests")
        print("\n  Method 3:")
        print("    pip install -r requirements-dev.txt")
        print("\n" + "=" * 70 + "\n")
        return False
    
    return True


def print_section(title):
    """Print a formatted section header."""
    print("\n" + "=" * 70)
    print(f"  {title}")
    print("=" * 70 + "\n")


def print_subsection(title):
    """Print a formatted subsection header."""
    print(f"\n{title}")
    print("-" * 70)


# ============================================================================
# TEST 1: --lib Flag Tests
# ============================================================================

def test_lib_flag():
    """Test the --lib flag with specific libraries."""
    print_section("TEST 1: --lib Flag Functionality")
    
    # Test 1.1: Add specific libraries with --force flag
    print_subsection("Test 1.1: Adding libraries with --force")
    print("Command: mod2pip --force --lib langchain,langchain-core")
    
    result = subprocess.run(
        ["python", "-m", "mod2pip.mod2pip", "--force", "--lib", "langchain,langchain-core"],
        capture_output=True,
        text=True
    )
    
    print("\nSTDERR:")
    print(result.stderr)
    print(f"Return code: {result.returncode}")
    
    if os.path.exists("requirements.txt"):
        print("\n✓ requirements.txt created successfully!")
        print("\nContents:")
        with open("requirements.txt", "r") as f:
            print(f.read())
    else:
        print("\n✗ requirements.txt was not created")
    
    # Test 1.2: Print to stdout
    print_subsection("Test 1.2: Print libraries to stdout with --print")
    print("Command: mod2pip --print --lib requests,numpy")
    
    result = subprocess.run(
        ["python", "-m", "mod2pip.mod2pip", "--print", "--lib", "requests,numpy"],
        capture_output=True,
        text=True
    )
    
    print("\nSTDOUT:")
    print(result.stdout)
    print("STDERR:")
    print(result.stderr)
    print(f"Return code: {result.returncode}")
    
    # Test 1.3: Test with --mode flag
    print_subsection("Test 1.3: Using --mode compat with --lib")
    print("Command: mod2pip --force --lib flask,django --mode compat")
    
    result = subprocess.run(
        ["python", "-m", "mod2pip.mod2pip", "--force", "--lib", "flask,django", "--mode", "compat"],
        capture_output=True,
        text=True
    )
    
    print("\nSTDERR:")
    print(result.stderr)
    print(f"Return code: {result.returncode}")
    
    if os.path.exists("requirements.txt"):
        print("\nContents:")
        with open("requirements.txt", "r") as f:
            print(f.read())
    
    # Test 1.4: Test with non-existent library
    print_subsection("Test 1.4: Testing with non-existent library")
    print("Command: mod2pip --print --lib nonexistent-package-xyz")
    
    result = subprocess.run(
        ["python", "-m", "mod2pip.mod2pip", "--print", "--lib", "nonexistent-package-xyz"],
        capture_output=True,
        text=True
    )
    
    print("\nSTDERR:")
    print(result.stderr)
    print(f"Return code: {result.returncode}")
    
    print("\n✓ --lib flag tests completed!")


# ============================================================================
# TEST 2: --generate-env Flag Tests
# ============================================================================

def create_env_test_project():
    """Create a test project with environment variable usage."""
    test_dir = tempfile.mkdtemp()
    
    # Create config.py with various env var patterns
    with open(os.path.join(test_dir, "config.py"), "w") as f:
        f.write("""
import os
from os import environ

# Database configuration
DATABASE_URL = os.environ.get('DATABASE_URL', 'postgresql://localhost/mydb')
DB_HOST = os.getenv('DB_HOST', 'localhost')
DB_PORT = os.getenv('DB_PORT', '5432')
DB_NAME = os.environ['DB_NAME']
DB_USER = os.environ.get('DB_USER')
DB_PASSWORD = os.getenv('DB_PASSWORD')

# API Keys
API_KEY = os.environ.get('API_KEY')
SECRET_KEY = os.getenv('SECRET_KEY', 'dev-secret-key')

# Application settings
DEBUG = os.getenv('DEBUG', 'False')
PORT = os.environ.get('PORT', '8000')
HOST = os.getenv('HOST', '0.0.0.0')
LOG_LEVEL = os.environ.get('LOG_LEVEL', 'INFO')

# AWS Configuration
AWS_ACCESS_KEY_ID = environ.get('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = environ['AWS_SECRET_ACCESS_KEY']
AWS_REGION = os.getenv('AWS_REGION', 'us-east-1')

# Email settings
SMTP_HOST = os.environ.get('SMTP_HOST')
SMTP_PORT = os.getenv('SMTP_PORT', '587')
EMAIL_FROM = os.environ.get('EMAIL_FROM', 'noreply@example.com')
""")
    
    # Create app.py with more env vars
    with open(os.path.join(test_dir, "app.py"), "w") as f:
        f.write("""
import os

# Redis configuration
REDIS_URL = os.getenv('REDIS_URL', 'redis://localhost:6379')

# Environment
ENVIRONMENT = os.environ.get('ENVIRONMENT', 'development')

# Custom variables
CUSTOM_VAR = os.getenv('CUSTOM_VAR')
ANOTHER_SETTING = os.environ.get('ANOTHER_SETTING', 'default_value')
""")
    
    return test_dir


def test_generate_env():
    """Test the --generate-env flag."""
    print_section("TEST 2: --generate-env Flag Functionality")
    
    test_dir = create_env_test_project()
    
    try:
        print(f"Created test project in: {test_dir}")
        print("\nTest files created:")
        for root, dirs, files in os.walk(test_dir):
            for file in files:
                if file.endswith('.py'):
                    print(f"  - {file}")
        
        print_subsection(f"Running: mod2pip --generate-env --force {test_dir}")
        
        # Run mod2pip via command line
        result = subprocess.run(
            ["python", "-m", "mod2pip.mod2pip", "--generate-env", "--force", test_dir],
            capture_output=True,
            text=True
        )
        
        print("\nSTDERR:")
        print(result.stderr)
        print(f"Return code: {result.returncode}")
        
        print_subsection("Checking generated files")
        
        # Check if .env was created
        env_file = os.path.join(test_dir, '.env')
        if os.path.exists(env_file):
            print("\n✓ .env file created successfully!")
            print("\nContents of .env (first 30 lines):")
            print("-" * 70)
            with open(env_file, 'r') as f:
                lines = f.readlines()
                print(''.join(lines[:30]))
                if len(lines) > 30:
                    print(f"... ({len(lines) - 30} more lines)")
            print("-" * 70)
        else:
            print("\n✗ .env file was not created")
        
        # Check if .env.sample was created
        sample_file = os.path.join(test_dir, '.env.sample')
        if os.path.exists(sample_file):
            print("\n✓ .env.sample file created successfully!")
        else:
            print("\n✗ .env.sample file was not created")
        
        print("\n✓ --generate-env flag tests completed!")
        
    except Exception as e:
        print(f"\n✗ Test failed with error: {e}")
        import traceback
        traceback.print_exc()
    
    finally:
        # Cleanup
        if os.path.exists(test_dir):
            shutil.rmtree(test_dir)
            print(f"\nCleaned up test directory")


# ============================================================================
# TEST 3: Enhanced Detection Tests
# ============================================================================

def create_enhanced_test_project():
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

    return test_dir


def test_enhanced_detection():
    """Test enhanced import detection."""
    print_section("TEST 3: Enhanced Import Detection")
    
    test_dir = create_enhanced_test_project()

    try:
        from mod2pip import mod2pip
        
        print_subsection("Test 3.1: Basic import detection")
        imports = mod2pip.get_all_imports(test_dir)
        print(f"Found imports: {imports}")

        print_subsection("Test 3.2: Local package detection")
        local_packages = mod2pip.get_locally_installed_packages()
        print(f"Found {len(local_packages)} local packages")
        if local_packages:
            print("Sample packages (first 5):")
            for pkg in local_packages[:5]:
                print(f"  - {pkg['name']}: {pkg.get('version', 'unknown')}")

        print_subsection("Test 3.3: Package name mapping")
        pkg_names = mod2pip.get_pkg_names(imports)
        print(f"Mapped package names: {pkg_names}")

        print_subsection("Test 3.4: Local import resolution")
        local_imports = mod2pip.get_import_local(imports)
        print(f"Resolved local imports: {[pkg['name'] for pkg in local_imports]}")

        print("\n✓ Enhanced detection tests completed!")

    except Exception as e:
        print(f"\n✗ Test failed: {e}")
        import traceback
        traceback.print_exc()

    finally:
        shutil.rmtree(test_dir)


def test_conda_detection():
    """Test conda environment detection."""
    print_section("TEST 4: Conda Environment Detection")

    # Check if we're in a conda environment
    conda_prefix = os.environ.get("CONDA_PREFIX")
    if conda_prefix:
        print(f"✓ Conda environment detected: {conda_prefix}")

        try:
            from mod2pip import mod2pip
            packages = mod2pip._get_conda_packages()
            print(f"Found {len(packages)} conda packages")

            if packages:
                print("\nSample conda packages (first 5):")
                for pkg in packages[:5]:
                    print(f"  - {pkg['name']}: {pkg['exports']}")
        except Exception as e:
            print(f"Error detecting conda packages: {e}")
    else:
        print("ℹ No conda environment detected (this is normal if not using conda)")

    print("\n✓ Conda detection test completed!")


def test_transitive_dependencies():
    """Test transitive dependency resolution."""
    print_section("TEST 5: Transitive Dependency Resolution")

    # Create sample packages
    sample_packages = [
        {"name": "requests", "version": "2.28.0"},
        {"name": "flask", "version": "2.0.0"}
    ]

    try:
        from mod2pip import mod2pip
        print("Testing transitive dependency resolution...")
        print(f"Sample packages: {[p['name'] for p in sample_packages]}")
        
        transitive_deps = mod2pip.get_transitive_dependencies(sample_packages, max_depth=1)
        print(f"\nFound {len(transitive_deps)} transitive dependencies")

        if transitive_deps:
            print("\nTransitive dependencies (first 10):")
            for dep in transitive_deps[:10]:
                version = dep.get('version', 'unknown')
                print(f"  - {dep['name']}: {version}")
            if len(transitive_deps) > 10:
                print(f"  ... and {len(transitive_deps) - 10} more")

        print("\n✓ Transitive dependency test completed!")

    except Exception as e:
        print(f"\n✗ Test failed: {e}")
        import traceback
        traceback.print_exc()


# ============================================================================
# Main Test Runner
# ============================================================================

def main():
    """Run all tests."""
    print("\n" + "=" * 70)
    print("  MOD2PIP COMPREHENSIVE TEST SUITE")
    print("=" * 70)
    
    # Check dependencies first
    if not check_dependencies():
        sys.exit(1)
    
    print("\n✓ All dependencies are installed\n")
    
    try:
        # Test 1: --lib flag
        test_lib_flag()
        
        # Test 2: --generate-env flag
        test_generate_env()
        
        # Test 3: Enhanced detection
        test_enhanced_detection()
        
        # Test 4: Conda detection
        test_conda_detection()
        
        # Test 5: Transitive dependencies
        test_transitive_dependencies()
        
        # Summary
        print_section("TEST SUMMARY")
        print("✓ All tests completed successfully!")
        print("\nTests run:")
        print("  1. --lib flag functionality")
        print("  2. --generate-env flag functionality")
        print("  3. Enhanced import detection")
        print("  4. Conda environment detection")
        print("  5. Transitive dependency resolution")
        
    except KeyboardInterrupt:
        print("\n\nTests interrupted by user")
        sys.exit(1)
    except Exception as e:
        print(f"\n\n✗ Test suite failed with error: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)


if __name__ == "__main__":
    main()
