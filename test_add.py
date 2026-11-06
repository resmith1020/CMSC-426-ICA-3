import unittest
from add import addition

class TestAdd(unittest.TestCase):
    def test_addition(self):
        result = addition(9, 10)
        self.assertEqual(result, 19)

if __name__ == "__main__":
    print("Application Started")
    unittest.main()
    print("10 + 9 =", add.addition(10, 9))
