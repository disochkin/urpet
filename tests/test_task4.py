from unittest import TestCase
import task4

class Test(TestCase):
    def test_get_swapped_min_max_array(self):
        self.assertEqual(task4.get_swapped_min_max_array([1, 3, 4, 6]), [6, 3, 4, 1])
        self.assertEqual(task4.get_swapped_min_max_array([1, 3]), [3, 1])
        self.assertEqual(task4.get_swapped_min_max_array([1, 3]), [3, 1])
        self.assertEqual(task4.get_swapped_min_max_array([1, 1, 1, 1]), [1, 1, 1, 1])
        self.assertEqual(task4.get_swapped_min_max_array([5, 10, 1, 5]), [5, 1, 10, 5])

