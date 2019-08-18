import  unittest
from question1_a import LoanMgt


class TestLoanMgt(unittest.TestCase):

    def test_lonmgt1(self):
        result = question1_a.LoanMgt(3000, 3, 500, 10, 1500, 7, 700000)
        self.assertEqual(result, 144)

    def test_lonmgt2(self):
        result = question1_a.LoanMgt(500, 3, 500, 10, 500, 7, 21000)
        self.assertEqual(result, 17)

    def test_lonmgt3(self):
        result = question1_a.LoanMgt(1300, 0, 500, 0, 1500, 7, 10000)
        self.assertEqual(result, 6)
    
    def test_lonmgt4(self):
        result = question1_a.LoanMgt(1000, 3, 500, 10, 1500, 7, 11000)
        self.assertEqual(result, 6)

if __name__ == '__main__':
    unittest.main()