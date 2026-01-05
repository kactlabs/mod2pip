#!/usr/bin/env python
"""
Simple compatibility test for mod2pip across Python versions.
"""

import sys
import os

# Add the current directory to Python path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

def test_basic_import():
    """Test that we can import the main module."""
    try:
        from mod2pip import mod2pip
        print(f"✅ Successfully imported mod2pip on Python {sys.version}")
        return True
    except ImportError as e:
        print(f"❌ Failed to import mod2pip: {e}")
        return False

def test_basic_functionality():
    """Test basic functionality."""
    try:
        from mod2pip import mod2pip
        
        # Test basic function
        test_dir = os.path.join(os.path.dirname(__file__), "tests", "_data")
        if os.path.exists(test_dir):
            imports = mod2pip.get_all_imports(test_dir)
            print(f"✅ Basic functionality works: found {len(imports)} imports")
            return True
        else:
            print("⚠️  Test data directory not found, skipping functionality test")
            return True
    except Exception as e:
        print(f"❌ Basic functionality failed: {e}")
        return False

def main():
    """Run compatibility tests."""
    print(f"Running compatibility tests on Python {sys.version}")
    print("=" * 60)
    
    tests = [
        ("Import Test", test_basic_import),
        ("Functionality Test", test_basic_functionality),
    ]
    
    passed = 0
    total = len(tests)
    
    for test_name, test_func in tests:
        print(f"\n🧪 {test_name}:")
        if test_func():
            passed += 1
    
    print("\n" + "=" * 60)
    print(f"Results: {passed}/{total} tests passed")
    
    if passed == total:
        print("🎉 All compatibility tests passed!")
        return 0
    else:
        print("💥 Some tests failed!")
        return 1

if __name__ == "__main__":
    sys.exit(main())