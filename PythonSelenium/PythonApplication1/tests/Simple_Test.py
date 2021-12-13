import unittest

class Test_Simple_Test(unittest.TestCase):
    def test_A(self):
        self.assertFalse(False);

if __name__ == '__main__':
    unittest.main()
