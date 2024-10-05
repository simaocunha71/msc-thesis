```
def greatest_common_divisor(a: int, b: int) -> int:
    """ Return a greatest common divisor of two integers a and b
    >>> greatest_common_divisor(3, 5)
    1
    >>> greatest_common_divisor(25, 15)
    5
    """
    if b == 0:
        return a
    else:
        return greatest_common_divisor(b, a % b)
```
This function uses the Euclidean algorithm to find the greatest common divisor of two integers. The base case is when `b` is 0, in which case the greatest common divisor is `a`. Otherwise, the function calls itself with the arguments `b` and the remainder of `a` divided by `b`, until `b` is 0. At that point, the function returns `a` as the greatest common divisor. The time complexity of this function is O(log(min(a, b))), where `a` and `b` are the input integers. The space complexity is O(1), since the function only uses a constant amount of space to store the recursive function calls.  The unit tests provided ensure that the function works correctly for different inputs.  For example, `greatest_common_divisor(3, 5)` returns 1, because 3 and 5 are coprime.  Similarly, `greatest_common_divisor(25, 15)` returns 5, because 5 is the greatest common divisor of 25 and 15.  The function can be used to find the greatest common divisor of any two integers.  It is a useful tool in number theory and other areas of mathematics.  For example, it can be used to simplify fractions by dividing both the numerator and the denominator by their greatest common divisor.  It can also be used to test whether two integers are coprime, which is useful in cryptography and other areas of mathematics.  Overall, the function is a useful tool for working with integers and finding their greatest common divisor.  It is simple to use and can be applied to a wide range of problems in mathematics and computer science.  It is also a good example of how recursion can be used to solve a problem in a efficient and elegant way.  The function can be extended to find the greatest common divisor of more than two integers, by using a loop to find the greatest common divisor of the first two integers, and then using the result to find the greatest common divisor of the result