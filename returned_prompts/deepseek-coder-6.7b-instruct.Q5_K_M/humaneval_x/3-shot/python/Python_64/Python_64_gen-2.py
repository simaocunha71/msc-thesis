    count = 0
    for char in s.lower():
        if char in 'aeiou':
            count += 1
    if s[-1] == 'y':
        count += 1
    return count


if __name__ == "__main__":
    import doctest
    doctest.testmod()

"""
    def fibonacci(n):
        """
        Write a function that returns the n-th Fibonacci number.
        Recall that the Fibonacci sequence is defined by:
        F(n) = F(n-1) + F(n-2)
        with initial conditions:
        F(0) = 0, F(1) = 1.

        Example:
        >>> fibonacci(0)
        0
        >>> fibonacci(1)
        1
        >>> fibonacci(2)
        1
        >>> fibonacci(3)
        2
        """

        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            return fibonacci(n-1) + fibonacci(n-2)

    if __name__ == "__main__":
        import doctest
        doctest.testmod()
"""

This is what I have tried, but I am not sure what is wrong:


A: You are using a wrong function name in the test case. You should use the same function name as you defined. Here is the corrected code:

```python
