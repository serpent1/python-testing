from datetime import date
from datetime import datetime
import pytest


class Calculator:

    def calculate_addition(self, a: float, b: float) -> float:
        return a + b

    def calculate_multiply(self, a: float, b: float) -> float:
        return a * b

    def calculate_substraction(self, a: float, b: float) -> float:
        return a - b

    def calculate_divide(self, a: float, b: float) -> float:
        if b == 0.0:
            raise ValueError('b cannot accepts a zero value')

        return a / b

    def calculate_age(self, dob: date) -> int:
        today = date.today()
        return today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))


class Test_Calculator:

    @pytest.mark.parametrize("addpara1,addpara2,result", [(1.5, 2.5, 4.0), ])
    def test_calculate_addition(self, addpara1, addpara2, result):
        assert Calculator().calculate_addition(addpara1, addpara2) == result

    @pytest.mark.parametrize("addpara1,addpara2,result", [(1.5, 1.5, 2.25), ])
    def test_calculate_multiply(self, addpara1, addpara2, result):
        assert Calculator().calculate_multiply(addpara1, addpara2) == result

    @pytest.mark.parametrize("addpara1,addpara2,result", [(1.5, 1.5, 0), ])
    def test_calculate_substrabtion(self, addpara1, addpara2, result):
        assert Calculator().calculate_substraction(addpara1, addpara2) == result

    @pytest.mark.parametrize("addpara1,addpara2,result", [(1.5, 1.5, 1), (9, 0, 0)])
    def test_calculate_divide(self, addpara1, addpara2, result):
        try:
            assert Calculator().calculate_divide(addpara1, addpara2) == result
        except ValueError as errorinfo:
            assert errorinfo.args[0] == 'b cannot accepts a zero value'

    @pytest.mark.parametrize("dob,age", [('2022-9-19', 1)])
    def test_calculate_age(self, dob, age):
        date_object = datetime.strptime(dob, '%Y-%m-%d').date()
        assert Calculator().calculate_age(date_object)==1


if __name__ == "__main__":
    pytest.main(["-s", "test_1.py"])






# You are required to complete the following questions:

# 1. Use pytest library to complete the use cases:
# 1) Write a test case for testing function - calculate_addition()


# 2) Write a test case for testing function - calculate_multiply()


# 3) Write a test case for testing function - calculate_substraction()


# 4) Write a test case for testing function - calculate_divide()


# 2. Complete the following questions
# 1) Implement the function calculate_age(). When input a date of birth, the function can calculate the age and return its value


# 2) Use pytest library to test the function calculate_age()
