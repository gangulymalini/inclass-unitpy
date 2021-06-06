import unittest
import palindrome


class TestCase(unittest.TestCase):
    def test_1(self):
        self.assertEqual(palindrome.palindrometester("madam"), True)
    def test_2(self):
        self.assertEqual(palindrome.palindrometester("racecar"), True)
    def test_3(self):
        self.assertEqual(palindrome.palindrometester("you're ugly"), False)


if __name__ == "__main__":
    unittest.main()