#!/usr/bin/env python
"""Demo project to test enhanced mod2pip functionality."""

# Static imports
import requests
import numpy as np
from flask import Flask

# Dynamic imports that regular pipreqs would miss
import importlib
pandas_module = importlib.import_module('pandas')

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

# String-based dynamic import
module_name = "matplotlib"
plt = __import__(module_name + ".pyplot", fromlist=[''])

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello World!"

if __name__ == '__main__':
    app.run()