```
def is_perfect_square(n):
    if n < 0:
        return False
    if n == 0 or n == 1:
        return True
    i = 1
    while i * i <= n:
        if i * i == n:
            return True
        i += 1
    return False
```
The function checks whether the given number is a perfect square or not. It starts by checking if the number is less than 0, in which case it is not a perfect square. Then it checks if the number is 0 or 1, in which case it is a perfect square. Then it enters a loop where it checks if the square of the current number is equal to the given number. If it finds a match, it returns True. If it doesn't find a match after checking all numbers up to the square root of the given number, it returns False.

The unit test `assert not is_perfect_square(10)` ensures that the function correctly identifies non-perfect squares. 
For example, 10 is not a perfect square, so the function should return False. 

The time complexity of this function is O(sqrt(n)), where n is the input number. This is because it needs to iterate up to the square root of the number to check if it's a perfect square. The space complexity is O(1), which means it uses a constant amount of space. 