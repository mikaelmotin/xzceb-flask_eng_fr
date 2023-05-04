import translator
import unittest

class testWatsonTranslator(unittest.TestCase):
    def test_english_to_French(self):
        self.assertEqual(translator.english_to_french("Hello"), "Bonjour")

    def test_french_to_english(self):
        self.assertEqual(translator.french_to_english("Bonjour"), "Hello")


if __name__ == '__main__':
    unittest.main()
