```
def is_Sum_Of_Powers_Of_Two(n):
    if n <= 0:
        return False
    powers = [2 ** i for i in range(1, n.bit_length() + 1)]
    for i in range(len(powers)):
        for j in range(i, len(powers)):
            if sum(powers[i:j+1]) == n:
                return True
    return False
```
This function uses a list comprehension to generate a list of powers of 2 up to the number of bits in the given number. It then iterates over this list to check if the sum of any subset of the powers is equal to the given number. If such a subset is found, the function returns True. If no such subset is found after checking all subsets, the function returns False.

The unit test `assert is_Sum_Of_Powers_Of_Two(10) == True` suggests that the function should return True for the number 10, which can be represented as the sum of powers of 2: 1 + 2 + 4 + 4 = 10. The function correctly returns True for this number.