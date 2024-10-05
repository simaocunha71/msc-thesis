    def is_simple_power(x, n):
        while x > 1:
            if x % n != 0:
                return False
            x = x // n
        return True










# Python3 program to check if a
# number is power of 2 or not

# Function to check if a number
# is power of 2 or not
def isPowerOfTwo(n) :
    # Check if n is a power of 2
    return (n & (n - 1)) == 0

# Driver program
n = 1
while True:
    x = n
    while True:
        if x % 2 != 0:
            break
        x = x // 2
    if x != 1:
        break
    if isPowerOfTwo(n):
        print(True)
    else:
        print(False)
    n += 1
```