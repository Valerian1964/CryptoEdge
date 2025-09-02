# test_cryptoedge.py
"""
Tests for CryptoEdge module.
"""

import unittest
from cryptoedge import CryptoEdge

class TestCryptoEdge(unittest.TestCase):
    """Test cases for CryptoEdge class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = CryptoEdge()
        self.assertIsInstance(instance, CryptoEdge)
        
    def test_run_method(self):
        """Test the run method."""
        instance = CryptoEdge()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
