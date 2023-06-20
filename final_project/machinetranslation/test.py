import unittest
from translator import english_to_french, french_to_english


class TestEnglishToFrench(unittest.TestCase):
    def test_equalEnglishToFrecnh(self):
        self.assertEqual(english_to_french('Hello'),'Bonjour')

    def test_notEqualEnglishToFrench(self):
        self.assertNotEqual(english_to_french('Hello'),'Bonjour')

class TestFrenchToEnglish(unittest.TestCase):
    def test_equalFrenchToEnglish(self):
        self.assertEqual(french_to_english('Bonjour'),'Hello')
    
    def test_notEqualFrenchToEnglis(self):
        self.assertNotEqual(french_to_english('abc'),'Hello')

if __name__=='__main__':
    unittest.main()