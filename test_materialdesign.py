# test_materialdesign.py
"""
Tests for MaterialDesign module.
"""

import unittest
from materialdesign import MaterialDesign

class TestMaterialDesign(unittest.TestCase):
    """Test cases for MaterialDesign class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = MaterialDesign()
        self.assertIsInstance(instance, MaterialDesign)
        
    def test_run_method(self):
        """Test the run method."""
        instance = MaterialDesign()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
