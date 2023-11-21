import unittest
from io import StringIO
from unittest.mock import patch
from main import PalavrasObserver

class TestPalavrasObserver(unittest.TestCase):

    def setUp(self):
        self.observer = PalavrasObserver()

    def test_update_output(self):
        with patch('sys.stdout', new=StringIO()) as fake_output:
            self.observer.update("Isso e um teste")
            expected_output = "Total de palavras: 4\nPalavras com quantidade par de caracteres: 2\nPalavras começadas com maiúsculas: 1\n"
            self.assertEqual(fake_output.getvalue(), expected_output)

    def test_update_empty_input(self):
        with patch('sys.stdout', new=StringIO()) as fake_output:
            self.observer.update("")
            expected_output = "Total de palavras: 0\nPalavras com quantidade par de caracteres: 0\nPalavras começadas com maiúsculas: 0\n"
            self.assertEqual(fake_output.getvalue(), expected_output)

    def test_update_all_uppercase_words(self):
        with patch('sys.stdout', new=StringIO()) as fake_output:
            self.observer.update("TUDO EM MAIUSCULO")
            expected_output = "Total de palavras: 3\nPalavras com quantidade par de caracteres: 2\nPalavras começadas com maiúsculas: 3\n"
            self.assertEqual(fake_output.getvalue(), expected_output)

    def test_update_single_lowercase_word(self):
        with patch('sys.stdout', new=StringIO()) as fake_output:
            self.observer.update("oi")
            expected_output = "Total de palavras: 1\nPalavras com quantidade par de caracteres: 1\nPalavras começadas com maiúsculas: 0\n"
            self.assertEqual(fake_output.getvalue(), expected_output)

if __name__ == '__main__':
    unittest.main()
