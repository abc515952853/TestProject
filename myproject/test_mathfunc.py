import unittest
from mathfunc import *
import ddt
class TestMathFunc(unittest.TestCase):
    """Test mathfuc.py"""

    @classmethod
    def setUpClass(cls):
        print ("This setUpClass() method only called once.")

    @classmethod
    def tearDownClass(cls):
        print ("This tearDownClass() method only called once too.")

    @ddt.data(1)  
    def test_add(self):
        """Test method add(a, b)"""
        self.assertNotEqual(-1, add(2, 2))
        # self.assertNotEqual(3, add(2, 2))


    # def test_minus(self):
    #     """Test method minus(a, b)"""
    #     self.assertEqual(1, minus(3, 2))
    #     self.assertNotEqual(4, minus(3, 2))


    # def test_multi(self):
    #     """Test method multi(a, b)"""
    #     self.assertEqual(6, multi(2, 3))

    # def test_divide(self):
    #     """Test method divide(a, b)"""
    #     self.assertEqual(2, divide(6, 3))
    #     self.assertEqual(2.5, divide(5, 2))
    # def test(self):
    #     """Test method divide(a, b)"""
    #     self.assertEqual(2, divide(6, 3))
    #     self.assertEqual(2.5, divide(5, 2))


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestMathFunc)  
    unittest.TextTestRunner(verbosity=2).run(suite)  