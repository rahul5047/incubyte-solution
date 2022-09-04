import unittest
from  StringCalculator import *

class TestAdd(unittest.TestCase):
    
    def test_for_empty_string(self):
        self.assertEqual(add(""),0)
    
    def test_for_one_number(self):
        self.assertEqual(add("1"),1)
        
    def test_for_empty_two_number(self):
        self.assertEqual(add("1,2"),3)
    
    