```
def next_smallest_palindrome(n):
    n += 1
    while not str(n) == str(n)[::-1]:
        n += 1
    return n
```
The function `next_smallest_palindrome` takes an integer `n` as input, adds 1 to it, and then checks if the resulting number is a palindrome. If not, it adds 1 again and checks again, and so on, until it finds a palindrome. The first palindrome found is the next smallest palindrome of the original number, which is then returned as the output. 

The unit test `assert next_smallest_palindrome(99)==101` ensures that the function works correctly for the given input. 

For example, if the input is 99, the function will add 1 to get 100, which is not a palindrome. It will then add 1 again to get 101, which is a palindrome, and return it as the next smallest palindrome. 