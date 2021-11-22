import calculator
import unittest
from unittest.mock import patch
from io import StringIO
import sys

class TestCalculator(unittest.TestCase):
    
    @patch("sys.stdin", StringIO("not numbers\nsome 1 or 2 numbers\n1,2,3,4,5,6\n2,2\n"))
    def test_get_input(self):
        """ this checks that if if any item in the list is non numeric the loop asks 
        for input until only numbers are entered by the user"""

        self.assertEqual(calculator.get_input(), [2,2])

    def test_get_only_two_numbers(self):
        """this checks that we receive exactly 2 numbers from user, no more or less"""
        
        self.assertTrue(calculator.only_two_numbers("1,2,3") ==False)
        self.assertTrue(calculator.only_two_numbers("1") == False)
        self.assertTrue(calculator.only_two_numbers("2,2") == True)
        

    def test_valid_list(self):
        """ this checks that our validator will only approve a list of numbers and reject it 
        if there is a non numeric"""

        self.assertTrue(calculator.is_valid("1,2,3,4,5"),True)
        self.assertTrue(calculator.is_valid("1,2,3,me,4,5") == False)

    @patch("sys.stdin", StringIO("%\n+\n"))
    def test_get_operator(self):
        """ this checks that the loop will continue to ask for an operator until we get a valid 
        operator for our calculator"""

        self.assertTrue(calculator.get_operator(),'+')

    def test_calculate(self):
        """"checks that given each operation we get the result expected"""

        sys_orig = sys.stdout
        my_file = StringIO()
        sys.stdout = my_file #Just to ensure that tests do not print anything out

        self.assertTrue(calculator.calculate([1,2],'+') == 3)
        self.assertTrue(calculator.calculate([2,2],'-') == 0)
        self.assertTrue(calculator.calculate([3,3],'/') == 1)
        self.assertTrue(calculator.calculate([4,4],'*') == 16)

    @patch("sys.stdin", StringIO("4,4\n*\noff\n"))
    def test_output_for_all_right_inputs(self):
        """this captures the program output and tests that the program gives the exact output
        we expect when perfectly valid input is entered
        """
        sys_orig = sys.stdout
        my_file = StringIO()

        sys.stdout = my_file 
        calculator.run()
        out_put = my_file.getvalue() #actually capturing the output so that we can test it

        self.assertEqual("""Welcome friend ! lets go !\n Please enter 2 numbers seperated by a comma :\nPlease choose and operator : + ,- ,/ ,* :\nThe result is : 16\n Please enter 2 numbers seperated by a comma :\n""",out_put)
        
        sys.stdout = sys_orig

    

if __name__=="__main__":
    unittest.main()