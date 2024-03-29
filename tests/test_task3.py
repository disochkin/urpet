from unittest import TestCase
import task3

class Test(TestCase):
    def test_check_contain_redundance_digits(self):
        self.assertEqual(task3.check_contain_redundance_digits('123'), 'YES')
        self.assertEqual(task3.check_contain_redundance_digits('333'), 'NO')
        self.assertEqual(task3.check_contain_redundance_digits('121'), 'NO')
        self.assertEqual(task3.check_contain_redundance_digits('0980'), 'NO')
        self.assertEqual(task3.check_contain_redundance_digits('6789'), 'YES')


