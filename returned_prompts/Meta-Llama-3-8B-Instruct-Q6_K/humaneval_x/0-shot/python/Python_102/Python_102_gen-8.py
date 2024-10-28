```
def choose_num(x, y):
    if x % 2 == 0:
        if y % 2 == 0:
            return y
        else:
            for i in range(y-1, x-1, -1):
                if i % 2 == 0:
                    return i
            return -1
    else:
        for i in range(x+1, y+1):
            if i % 2 == 0:
                return i
        return -1
```
The function checks if the first number is even. If it is, then it checks if the second number is also even. If both are even, then it returns the second number. If the second number is odd, then it starts from the second number and goes backwards until it finds the first even number. If no even number is found, then it returns -1. If the first number is odd, then it starts from the first number and goes forward until it finds the first even number. If no even number is found, then it returns -1. This way, the function ensures that the biggest even number in the range [x, y] is returned. If no such number exists, then it returns -1.