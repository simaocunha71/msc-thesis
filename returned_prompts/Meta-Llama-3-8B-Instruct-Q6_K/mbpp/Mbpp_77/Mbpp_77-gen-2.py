```
def is_Diff(n):
    n = str(n)
    return sum(int(digit) for digit in n) % 11 != 0
```
The function converts the number into a string, then iterates over each character (digit) in the string, converts it back into an integer, and sums them all up. The remainder of this sum when divided by 11 is checked. If it is not 0, the number is not divisible by 11 and the function returns False. If it is 0, the number is divisible by 11 and the function returns True. 

The unit test `assert is_Diff(12345) == False` indicates that the function should return False for the number 12345, which is indeed not divisible by 11. 