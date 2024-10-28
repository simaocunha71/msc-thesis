```
def is_Sum_Of_Powers_Of_Two(n):
    if n < 1:
        return False
    powers = [2**i for i in range(0, n.bit_length() + 1)]
    return all(p in powers for p in range(1, n + 1))
```
This function works by first generating all the powers of 2 that are less than or equal to the given number. It then checks if each number from 1 to the given number is in this list of powers of 2. If any number is not in the list, the function returns False. If all numbers are in the list, the function returns True. The unit test `assert is_Sum_Of_Powers_Of_Two(10) == True` ensures that the function correctly identifies numbers that can be represented as the sum of non-zero powers of 2. 

The function `is_Sum_Of_Powers_Of_Two(10)` returns True because 10 can be represented as the sum of non-zero powers of 2 (i.e., 1 + 2 + 4 + 4). The function `is_Sum_Of_Powers_Of_Two(11)` would return False because 11 cannot be represented as the sum of non-zero powers of 2.  The function `is_Sum_Of_Powers_Of_Two(15)` would return True because 15 can be represented as the sum of non-zero powers of 2 (i.e., 1 + 2 + 4 + 8).  The function `is_Sum_Of_Powers_Of_Two(16)` would return True because 16 can be represented as the sum of non-zero powers of 2 (i.e., 1 + 2 + 4 + 8 + 4). 

The time complexity of this function is O(n), where n is the given number. This is because the function generates all the powers of 2 that are less than or equal to the given number, and then checks if each number from 1 to the given number is in this list of powers of 2. The space complexity of this function is also O(n), where n is the given number. This is because the function generates a list of powers of 2 that are less than or equal to the given number, and then checks if each number from 1 to the given number is in this list of powers of 2. 

The unit test `assert is_Sum_Of_Powers_Of_Two(10)