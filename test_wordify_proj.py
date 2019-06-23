'''
 test_wordify_proj.py

 Revision : V1.0

 Last Modified Date    Author

 23-Jun-2019           Narain Massand
'''
import unittest
from wordify_proj import number_to_words, words_to_number

class TestUM(unittest.TestCase):

    def test_number_to_words(self):
        self.assertEqual(number_to_words('18007246837'), '1800PAINTER')
        self.assertEqual(number_to_words('1800-72837&&'), '1800-SAVER')
        self.assertEqual(number_to_words('1800 7246837'), '1800PAINTER')
        self.assertEqual(number_to_words('cbisncu88890024'), -1)
        self.assertEqual(number_to_words('11111111111111111111111'), -2)
        self.assertEqual(number_to_words('$#ED%RF&^G*GGB*&F&^'), -1)
        self.assertEqual(number_to_words('513-7625-7827'), '51FROCK7827')
        self.assertEqual(number_to_words('11111116262284595623'), '1111111MAMBA84595623')
        self.assertEqual(number_to_words('1111111111fedvcedcecw'), -1)
        self.assertEqual(number_to_words('00000000000000515151515848421111111111'), '00000000000000515151515VITI21111111111')

    def test_words_to_number(self):
        self.assertEqual(words_to_number('1-800-PAINTER'), '1-800-7246837')
        self.assertEqual(words_to_number('#$%^YTFR%'), -1)
        self.assertEqual(words_to_number('513-pickle robot'), '513-74255376268')
        self.assertEqual(words_to_number('1111111111000000000scscscscs'), '1111111111000000000727272727')
        self.assertEqual(words_to_number('911-ROCKSTAR'), '911-76257827')
        self.assertEqual(words_to_number('+1-800-TACO-bell'), '1-800-8226-2355')
        self.assertEqual(words_to_number('game-of-thrones'), '4263-63-8476637')
        self.assertEqual(words_to_number('$% ^&TU541515*Y  '), -1)
        self.assertEqual(words_to_number('lord-of-the-rings'), '5673-63-843-74647')
        self.assertEqual(words_to_number('513-HIRE-me'), '513-4473-63')

if __name__ == '__main__':
    unittest.main()
