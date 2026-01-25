#!/usr/bin/env python
"""
Test script for the --lib flag functionality.
"""

import subprocess
import os
import sys

def test_lib_flag():
    """Test the --lib flag with specific libraries."""
    print("Testing --lib flag functionality...\n")
    
    # Test 1: Add specific libraries with --force flag
    print("Test 1: Adding langchain and langchain-core with --force")
    print("Command: mod2pip --force --lib langchain,langchain-core")
    print("-" * 60)
    
    result = subprocess.run(
        ["python", "-m", "mod2pip.mod2pip", "--force", "--lib", "langchain,langchain-core"],
        capture_output=True,
        text=True
    )
    
    print("STDOUT:")
    print(result.stdout)
    print("\nSTDERR:")
    print(result.stderr)
    print("\nReturn code:", result.returncode)
    
    # Check if requirements.txt was created
    if os.path.exists("requirements.txt"):
        print("\n✓ requirements.txt created successfully!")
        print("\nContents of requirements.txt:")
        print("-" * 60)
        with open("requirements.txt", "r") as f:
            content = f.read()
            print(content)
        print("-" * 60)
    else:
        print("\n✗ requirements.txt was not created")
    
    print("\n" + "=" * 60 + "\n")
    
    # Test 2: Print to stdout instead of file
    print("Test 2: Print libraries to stdout with --print")
    print("Command: mod2pip --print --lib requests,numpy")
    print("-" * 60)
    
    result = subprocess.run(
        ["python", "-m", "mod2pip.mod2pip", "--print", "--lib", "requests,numpy"],
        capture_output=True,
        text=True
    )
    
    print("STDOUT:")
    print(result.stdout)
    print("\nSTDERR:")
    print(result.stderr)
    print("\nReturn code:", result.returncode)
    
    print("\n" + "=" * 60 + "\n")
    
    # Test 3: Test with --mode flag
    print("Test 3: Using --mode compat with --lib")
    print("Command: mod2pip --force --lib flask,django --mode compat")
    print("-" * 60)
    
    result = subprocess.run(
        ["python", "-m", "mod2pip.mod2pip", "--force", "--lib", "flask,django", "--mode", "compat"],
        capture_output=True,
        text=True
    )
    
    print("STDOUT:")
    print(result.stdout)
    print("\nSTDERR:")
    print(result.stderr)
    print("\nReturn code:", result.returncode)
    
    if os.path.exists("requirements.txt"):
        print("\nContents of requirements.txt:")
        print("-" * 60)
        with open("requirements.txt", "r") as f:
            content = f.read()
            print(content)
        print("-" * 60)
    
    print("\n" + "=" * 60 + "\n")
    
    # Test 4: Test with library that might not be installed
    print("Test 4: Testing with a library that might not be installed")
    print("Command: mod2pip --print --lib nonexistent-package-xyz")
    print("-" * 60)
    
    result = subprocess.run(
        ["python", "-m", "mod2pip.mod2pip", "--print", "--lib", "nonexistent-package-xyz"],
        capture_output=True,
        text=True
    )
    
    print("STDOUT:")
    print(result.stdout)
    print("\nSTDERR:")
    print(result.stderr)
    print("\nReturn code:", result.returncode)
    
    print("\n" + "=" * 60 + "\n")
    print("All tests completed!")

if __name__ == "__main__":
    test_lib_flag()
