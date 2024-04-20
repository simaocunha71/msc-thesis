"""
Write a python function that takes in a positive integer n and finds the sum of even index binomial coefficients.
assert even_binomial_Coeff_Sum(4) == 8
"""
from typing import Callable, Union
import math
from typing import Sequence
class Even_Binomial_Coeff():
    """Write a python function that takes in positive integer n and finds the sum of even index binomial coefficients."""
    def __init__(self) -> None:
        pass
    @staticmethod
    def even_binomial_Coeff_Sum(n:int):
        return _Even_Binomial_Coeffs(n).sum()
class _Even_Binomial_Coeffs():
    """
Write a class _Even_Binomial_Coeffs that represents the even index binomial coefficients
as defined in the problem statement.
"""
    def __init__(self, n:int) -> None:
        self.n = n
    @staticmethod
    def sum(index:Union[int, Sequence]) -> Union[float, int]:
        """
        Return the sum of binomial coefficients with index 0 .. n where i and j are even numbers.
        The function should return 0 in case any index is negative or 1 if index > n.
        """
        # print(index)
        
        pass # your code here
class TestEven_Binomial():
    """Define a class that creates some test data for the input of _Even_Binomial_Coeffs."""
    def __init__(self, n:int) -> None:
        self.n = n
        
def main() -> None:
    if not isinstance(Even_Binomial(), Even_Binomial():
        print("TypeError: Type " + str(type(Even_Binomial())) + " is not a valid type for an instance of class Even_Binomial()")
    pass # your test code here
if __name__ == '__main__':
    even_binomial = Even_Binomial()
main()