import unittest
import word


class TestCase(unittest.TestCase):
    def test_1(self):
        self.assertEqual(word.wordtester("madam"), 1)
    def test_2(self):
        self.assertEqual(word.wordtester("racecar"), 1)
    def test_3(self):
        self.assertEqual(word.wordtester("you're ugly"), 2)


if __name__ == "__main__":
    unittest.main()