```
def next_Perfect_Square(n):
    i = 1
    while True:
        square = i * i
        if square > n:
            return square
        i += 1
```
This function works by starting with the first perfect square (1) and then checking each subsequent perfect square to see if it is greater than the input number. When it finds a perfect square that is greater than the input number, it returns that square. The function continues to check perfect squares until it finds one that is greater than the input number. 

For example, if the input number is 35, the function will check the perfect squares 1, 4, 9, 16, 25, and 36. It will return 36 because it is the first perfect square greater than 35. 

The function uses a while loop to keep checking perfect squares until it finds one that is greater than the input number. The loop continues until it finds the correct perfect square, at which point it returns that square. 

The function also uses a variable `i` to keep track of the current perfect square, starting with 1. It increments `i` by 1 each time it checks a perfect square, so that it can check the next perfect square in the sequence. 

This function assumes that the input number is a non-negative integer. If the input number is negative or not an integer, the function may not work correctly. 

The unit test `assert next_Perfect_Square(35) == 36` ensures that the function works correctly for the input number 35. It checks that the function returns 36, which is the next perfect square greater than 35. 

This function has a time complexity of O(sqrt(n)), where n is the input number. This is because it checks each perfect square up to the input number, and there are sqrt(n) perfect squares up to n. The function has a space complexity of O(1), because it only uses a constant amount of space to store the loop variable and the perfect square. 