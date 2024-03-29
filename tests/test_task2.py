from unittest import TestCase
import task2

class Test(TestCase):
    def test_get_super_fact(self):
        self.assertEqual(task2.get_super_fact(0), 1)
        self.assertEqual(task2.get_super_fact(1), 1)
        self.assertEqual(task2.get_super_fact(2), 2)
        self.assertEqual(task2.get_super_fact(3), 12)
        self.assertEqual(task2.get_super_fact(4), 288)
        self.assertEqual(task2.get_super_fact(5), 34560)
        self.assertEqual(task2.get_super_fact(6), 24883200)
        self.assertEqual(task2.get_super_fact(7), 125411328000)
        self.assertEqual(task2.get_super_fact(8), 5056584744960000)