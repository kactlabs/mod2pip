#!/usr/bin/env python3
"""
Debug script for CI environments to help identify issues.
"""
import sys
import os
import subprocess
import importlib.util

def check_environment():
    """Check the Python environment and key dependencies."""
    print("=== Environment Debug Information ===")
    print(f"Python version: {sys.version}")
    print(f"Python executable: {sys.executable}")
    print(f"Platform: {sys.platform}")
    print(f"Current working directory: {os.getcwd()}")
    print(f"PYTHONPATH: {os.environ.get('PYTHONPATH', 'Not set')}")
    
    # Check if mod2pip can be imported
    try:
        import mod2pip
        print(f"✅ mod2pip imported successfully, version: {mod2pip.__version__}")
    except ImportError as e:
        print(f"❌ Failed to import mod2pip: {e}")
        return False
    
    # Check key dependencies
    dependencies = ['yarg', 'docopt', 'requests', 'nbconvert', 'ipython']
    for dep in dependencies:
        try:
            spec = importlib.util.find_spec(dep)
            if spec is not None:
                module = importlib.import_module(dep)
                version = getattr(module, '__version__', 'unknown')
                print(f"✅ {dep}: {version}")
            else:
                print(f"❌ {dep}: not found")
        except Exception as e:
            print(f"❌ {dep}: error - {e}")
    
    return True

def run_basic_tests():
    """Run basic functionality tests."""
    print("\n=== Basic Functionality Tests ===")
    
    try:
        # Test basic import detection
        from mod2pip.mod2pip import get_all_imports
        
        # Create a simple test file
        test_content = """
import os
import sys
import requests
"""
        with open('test_imports.py', 'w') as f:
            f.write(test_content)
        
        imports = get_all_imports('.')
        print(f"✅ Import detection works, found {len(imports)} imports")
        
        # Clean up
        os.remove('test_imports.py')
        
        return True
        
    except Exception as e:
        print(f"❌ Basic functionality test failed: {e}")
        return False

def main():
    """Main debug function."""
    print("Starting CI Debug Script...")
    
    env_ok = check_environment()
    if not env_ok:
        sys.exit(1)
    
    test_ok = run_basic_tests()
    if not test_ok:
        sys.exit(1)
    
    print("\n✅ All debug checks passed!")

if __name__ == "__main__":
    main()