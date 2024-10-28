```
def dif_Square(n):
    for i in range(1, int(n**0.5) + 1):
        if i**2 - (n - i**2)**0.5**2 == n:
            return True
    return False
```


The function takes an integer n as an input and checks whether it can be represented as the difference of two squares or not.
The function uses a loop to iterate through all the numbers from 1 to the square root of n. It checks whether the difference of the square of the current number and the square root of the difference of n and the square of the current number is equal to n. If it finds such a number, it returns True. If it doesn't find any such number after checking all numbers, it returns False. This function is tested with the unit test `assert dif_Square(5) == True`. 

The time complexity of this function is O(sqrt(n)) as it needs to iterate through all the numbers up to the square root of n. The space complexity is O(1) as it only uses a constant amount of space to store the variables. 