import unittest
from test_mathfunc import TestMathFunc
from HTMLTestRunner import HTMLTestRunner

if __name__ =='__main__':
    suite = unittest.TestSuite()
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(TestMathFunc))

    with open('UnittestTextReport.html','wb') as f:
        runner = HTMLTestRunner(stream=f,title='MathFunc Test Report',description='generated by HTMLTestRunner.',verbosity=2)
        runner.run(suite) 