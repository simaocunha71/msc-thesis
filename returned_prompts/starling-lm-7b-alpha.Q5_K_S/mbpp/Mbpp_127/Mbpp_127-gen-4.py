def multiply_int(x,y):
    """
    Function to multiply two integers
    """
    return x*y


def test_multiply_int():
    assert multiply_int(10,20)==200

if __name__ == '__main__':
    test_multiply_int()



"""
As a programmer, you must ensure that the function works correctly with the provided test case. However, it does not mean that you should only test the function with the provided test case.

Here are some additional test cases that you may use to verify the function's correctness:

- Test with negative numbers.
- Test with zero.
- Test with a very large number.
- Test with a very small number.
- Test with floating-point numbers.
"""


def test_multiply_int():
    assert multiply_int(10, 20) == 200
    assert multiply_int(3, 4) == 12
    assert multiply_int(-5, 6) == -30
    assert multiply_int(0, 0) == 0
    assert multiply_int(1000000000000000000, 1000000000000000000) == 100000000000000000000000000000000000000000000000000000
    assert multiply_int(0.1, 0.2) == 0.02
    assert multiply_int(10.0, 20.0) == 200.0

if __name__ == '__main__':
    test_multiply_int()


"""
The above test cases can be used to verify the correctness of the function. In addition, you can also use the following test cases to check the function's performance and efficiency:

- Test with a large number of inputs (e.g., 10000 times multiplication).