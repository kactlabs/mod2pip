#!/usr/bin/env python
"""
Demo project to test mod2pip features.

This file demonstrates:
1. Various import patterns for testing import detection
2. Environment variable usage for testing --generate-env
3. Both static and dynamic imports

Usage:
    # Test import detection
    mod2pip --force
    
    # Test environment variable detection
    mod2pip --generate-env --force
    
    # Run the demo
    python demo_project.py
"""

import os
from os import environ

# ============================================================================
# SECTION 1: Static Imports (for testing import detection)
# ============================================================================

import requests
import numpy as np
from flask import Flask

# ============================================================================
# SECTION 2: Dynamic Imports (for testing enhanced detection)
# ============================================================================

# Dynamic imports that regular pipreqs would miss
import importlib

# Try to import pandas dynamically
try:
    pandas_module = importlib.import_module('pandas')
except ImportError:
    pandas_module = None

# Conditional import
try:
    import tensorflow as tf
except ImportError:
    tf = None

# Late import in function
def process_data():
    """Function with late import."""
    try:
        import scipy.stats as stats
        return stats.norm()
    except ImportError:
        return None

# __import__ usage
json_module = __import__('json')

# String-based dynamic import
try:
    module_name = "matplotlib"
    plt = __import__(module_name + ".pyplot", fromlist=[''])
except ImportError:
    plt = None

# ============================================================================
# SECTION 3: Environment Variables (for testing --generate-env)
# ============================================================================

# Database configuration
DATABASE_URL = os.environ.get('DATABASE_URL', 'postgresql://localhost/mydb')
DB_HOST = os.getenv('DB_HOST', 'localhost')
DB_PORT = os.getenv('DB_PORT', '5432')
DB_NAME = os.environ.get('DB_NAME')
DB_USER = os.environ.get('DB_USER')
DB_PASSWORD = os.getenv('DB_PASSWORD')

# API Keys
API_KEY = os.environ.get('API_KEY')
SECRET_KEY = os.getenv('SECRET_KEY', 'dev-secret-key-change-in-production')

# Application settings
DEBUG = os.getenv('DEBUG', 'False')
PORT = os.environ.get('PORT', '8000')
HOST = os.getenv('HOST', '0.0.0.0')
LOG_LEVEL = os.environ.get('LOG_LEVEL', 'INFO')
ENVIRONMENT = os.environ.get('ENVIRONMENT', 'development')

# AWS Configuration
AWS_ACCESS_KEY_ID = environ.get('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')
AWS_REGION = os.getenv('AWS_REGION', 'us-east-1')

# Redis configuration
REDIS_URL = os.getenv('REDIS_URL', 'redis://localhost:6379')

# Email settings
SMTP_HOST = os.environ.get('SMTP_HOST')
SMTP_PORT = os.getenv('SMTP_PORT', '587')
EMAIL_FROM = os.environ.get('EMAIL_FROM', 'noreply@example.com')

# Custom application variables
CUSTOM_VAR = os.getenv('CUSTOM_VAR')
ANOTHER_SETTING = os.environ.get('ANOTHER_SETTING', 'default_value')
FEATURE_FLAG = os.getenv('FEATURE_FLAG', 'enabled')

# ============================================================================
# SECTION 4: Flask Application
# ============================================================================

app = Flask(__name__)

@app.route('/')
def hello():
    """Simple hello world endpoint."""
    return f"Hello World! Environment: {ENVIRONMENT}"

@app.route('/config')
def show_config():
    """Show configuration (without sensitive data)."""
    config = {
        'environment': ENVIRONMENT,
        'debug': DEBUG,
        'host': HOST,
        'port': PORT,
        'log_level': LOG_LEVEL,
        'database_configured': bool(DATABASE_URL),
        'api_key_configured': bool(API_KEY),
        'redis_configured': bool(REDIS_URL),
    }
    return config

# ============================================================================
# SECTION 5: Main Function
# ============================================================================

def main():
    """Demo function showing environment variable usage."""
    print("=" * 70)
    print("  MOD2PIP DEMO PROJECT")
    print("=" * 70)
    print("\nConfiguration:")
    print(f"  Database URL: {DATABASE_URL}")
    print(f"  API Key: {'Set' if API_KEY else 'Not set'}")
    print(f"  Environment: {ENVIRONMENT}")
    print(f"  Debug mode: {DEBUG}")
    print(f"  Host: {HOST}")
    print(f"  Port: {PORT}")
    print(f"  Log Level: {LOG_LEVEL}")
    print(f"  Redis URL: {REDIS_URL}")
    print("\nImported modules:")
    try:
        print(f"  - requests: {requests.__version__}")
    except:
        print(f"  - requests: installed")
    try:
        print(f"  - numpy: {np.__version__}")
    except:
        print(f"  - numpy: installed")
    try:
        print(f"  - flask: {Flask.__version__ if hasattr(Flask, '__version__') else 'installed'}")
    except:
        print(f"  - flask: installed")
    print(f"  - pandas: {'loaded' if pandas_module else 'not installed'}")
    print(f"  - tensorflow: {'loaded' if tf else 'not installed'}")
    print(f"  - matplotlib: {'loaded' if plt else 'not installed'}")
    print("\nTo test mod2pip features:")
    print("  1. Generate requirements.txt:")
    print("     mod2pip --force")
    print("\n  2. Generate .env files:")
    print("     mod2pip --generate-env --force")
    print("\n  3. Add specific libraries:")
    print("     mod2pip --force --lib requests,numpy,flask")
    print("\n" + "=" * 70)


if __name__ == '__main__':
    main()
