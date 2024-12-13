import unittest
import UserFunctions

class TestFunctions(unittest.TestCase):

    def test_sum(self):
        UserFunctions.assertEqual(sum([1, 2, 3]), 6, "Should be 6")

if __name__ == '__main__':
    unittest.main()
