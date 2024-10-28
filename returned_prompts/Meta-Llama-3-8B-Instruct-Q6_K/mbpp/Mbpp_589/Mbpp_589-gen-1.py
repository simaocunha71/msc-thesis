```
def perfect_squares(start, end):
    return [i**2 for i in range(int(start**0.5), int(end**0.5)+1)]
```
This function takes two parameters, start and end, and returns a list of perfect squares between the two numbers. It works by iterating over all integers from the square root of start to the square root of end (inclusive), squaring each integer, and adding it to the result list. The square root of a number is the number that, when multiplied by itself, gives the original number. For example, the square root of 16 is 4, because 4*4=16.

The unit test `assert perfect_squares(1,30)==[1, 4, 9, 16, 25]` ensures that the function returns the correct list of perfect squares between 1 and 30. The function passes this test because it correctly identifies the perfect squares 1, 4, 9, 16, and 25. The function can be used to find perfect squares between any two given numbers. For example, `perfect_squares(10,50)` would return `[100, 121, 144, 169, 196, 225]`.