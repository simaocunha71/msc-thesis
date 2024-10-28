```
def validate(n):
    n = str(n)
    for i in n:
        if int(i) > 0 and n.count(i) > int(i):
            return False
    return True
```
This function first converts the integer to a string. Then it iterates over each character in the string. If the count of the character in the string is more than the character itself, it returns False. If it doesn't find any such character, it returns True. 

For example, for the input 1234, the function checks the frequency of each digit. The frequency of 1 is 1, the frequency of 2 is 1, the frequency of 3 is 1, and the frequency of 4 is 1. Since all frequencies are less than or equal to the digit itself, the function returns True. 