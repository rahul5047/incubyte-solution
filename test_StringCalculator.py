import unittest
from  StringCalculator import *

class TestAdd(unittest.TestCase):
    
    def test_for_empty_string(self):
        self.assertEqual(add(""),0)
    
    def test_for_one_number(self):
        self.assertEqual(add("1"),1)
        
    def test_for_empty_two_number(self):
        self.assertEqual(add("1,2"),3)
    
    def test_for_unknown_number(self):
        self.assertEqual(add("1,2,3,4,5"),15)
    def test_for_negative_number(self):
            self.assertRaises(Exception,add,"-3")
            
    def test_for_print_negative_number(self):
            self.assertRaises(Exception,add,"-3,-4")
    def test_for_Numbers_bigger_ignored(self):
        self.assertEqual(add("2,1001"),2)
        
    def test_for_handle_newline(self):
        self.assertEqual(add("2,\n,3"),5)
        
    def test_for_different_delimiter(self):
            self.assertEqual(add("//;\n1;2"),3)
    def test_for_alphanumeric_addition(self):
            self.assertEqual(add("1,2,a,c"),7)
    