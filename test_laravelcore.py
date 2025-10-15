# test_laravelcore.py
"""
Tests for LaravelCore module.
"""

import unittest
from laravelcore import LaravelCore

class TestLaravelCore(unittest.TestCase):
    """Test cases for LaravelCore class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = LaravelCore()
        self.assertIsInstance(instance, LaravelCore)
        
    def test_run_method(self):
        """Test the run method."""
        instance = LaravelCore()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
