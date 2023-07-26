import unittest

from translator import englishtofrench, frenchtoenglish

class TestEnglishToFrench(unittest.TestCase): 
    def test1(self): 
        self.assertEqual(englishtofrench('Hello'), 'Bonjour') 
        self.assertNotEqual(englishtofrench('Bye'), 'Bonjour') 
        

class TestFrenchToEnglish(unittest.TestCase): 
    def test1(self): 
        self.assertEqual(frenchtoenglish('Bonjour'), 'Hello') 
        self.assertNotEqual(frenchtoenglish('Bonjour'), 'Bye') 
        
unittest.main()