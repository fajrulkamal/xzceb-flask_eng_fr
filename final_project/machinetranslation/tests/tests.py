import unittest
from translator import english_to_french 
from translator import french_to_english
class TestAdd(unittest.TestCase):

    def test1(self):

        self.assertEqual(french_to_english('Bonjour'), 'Hello')
        self.assertEqual(english_to_french('Hello'), 'Bonjour')
        
        
        
        
    def test2(self):

        self.assertNotEqual(french_to_english('Hello'), 'Bonjour')
        self.assertNotEqual(english_to_french('Bonjour'), 'Hello')
    
    
        
        
    def test3(self):     
        
        self.assertIsNone(french_to_english(''))
        self.assertIsNone(english_to_french(''))   
        
        
        
        
if __name__ == '__main__':
    unittest.main()