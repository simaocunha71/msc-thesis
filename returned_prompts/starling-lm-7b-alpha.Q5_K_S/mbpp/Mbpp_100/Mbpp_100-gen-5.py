```
def next_smallest_palindrome(n):
    '''
    Find the next smallest palindrome of a specified integer
    '''
    n += 1
    while True:
        if str(n) == str(n)[::-1]:
            return n
        n += 1
```

In this implementation, we start from the next number of the input integer, and increment the number until we find a palindrome. Here are some test cases to validate the function:
```python
def test_next_smallest_palindrome():
    assert next_smallest_palindrome(99) == 101
    assert next_smallest_palindrome(10) == 11
    assert next_smallest_palindrome(999) == 1001
    assert next_smallest_palindrome(9999) == 10001

test_next_smallest_palindrome()
```

It should be noted that this function is not very efficient. There are more efficient approaches to finding the next smallest palindrome, such as by generating all palindromes up to a certain limit and checking which is the smallest one.

Here's an implementation of a more efficient approach:
```python
def next_smallest_palindrome(n):
    '''
    Find the next smallest palindrome of a specified integer
    '''
    if n % 9 == 0:  # All palindromes are divisible by 9
        return 9 * (11 ** (len(str(n)) - 1))
    return 9 * (11 ** (len(str(n)) - 1)) + (n % 9 - n % 9 + 1)
```

This implementation uses the fact that all palindromes are divisible by 9, and generates the next smallest palindrome by incrementing the last digit of the number.

Here are some test cases to validate the function:
```python
def test_next_smallest_palindrome():
    assert next_smallest_palindrome(99) == 101
    assert next_smallest_palindrome