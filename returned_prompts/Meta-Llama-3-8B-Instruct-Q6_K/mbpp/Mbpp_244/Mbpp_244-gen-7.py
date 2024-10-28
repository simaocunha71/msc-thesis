```
def next_Perfect_Square(n):
    i = int(n ** 0.5) + 1
    while True:
        square = i ** 2
        if square > n:
            return square
        i += 1
``` 

The function next_Perfect_Square takes an integer n as input and returns the next perfect square greater than n. It starts by initializing a variable i to the integer part of the square root of n plus one. Then it enters a loop where it calculates the square of i, checks if it is greater than n, and if so, returns the square. If not, it increments i and continues the loop. This process continues until it finds a perfect square greater than n, which it then returns. The unit test `assert next_Perfect_Square(35) == 36` ensures that the function works correctly. 

The time complexity of this function is O(sqrt(n)) because it iterates up to the square root of n. The space complexity is O(1) because it only uses a constant amount of space. 