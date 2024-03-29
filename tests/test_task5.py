from unittest import TestCase
import task5

class Test(TestCase):
    def test_check_number_is_power_of_two(self):
        self.assertEqual(task5.check_number_is_power_of_two(3), False)
        self.assertEqual(task5.check_number_is_power_of_two(0), False)
        self.assertEqual(task5.check_number_is_power_of_two(2), True)
        self.assertEqual(task5.check_number_is_power_of_two(5), False)
        self.assertEqual(task5.check_number_is_power_of_two(8), True)

