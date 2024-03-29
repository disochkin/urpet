from unittest import TestCase
import task1

class Test(TestCase):
    def test_get_digit_count(self):
        def test_get_digit_count(self):
            self.assertEqual(task1.get_digit_count('123'), 3)
            self.assertEqual(task1.get_digit_count('0'), 1)
            self.assertEqual(task1.get_digit_count('00001'), 5)
            self.assertEqual(task1.get_digit_count('1.1'), 2)
            self.assertEqual(task1.get_digit_count('-3.3'), 2)