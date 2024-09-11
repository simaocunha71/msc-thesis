"""
def check_Consecutive(list):
    for i in range(len(list)-1):
        if list[i+1]-list[i] != 1:
            return False
    return True
"""

def check_Consecutive(list):
    return all(list[i+1]-list[i] == 1 for i in range(len(list)-1))

assert check_Consecutive([1,2,3,4,5]) == True
assert check_Consecutive([1,2,3,6,5]) == False


# Python3 program to check if a number is power of 2 or not
def isPowerOfTwo(n):
    return (n > 0) and ((n & (n - 1)) == 0)


# Driver code
if __name__ == "__main__":
    n = 32
    if (isPowerOfTwo(n)):
        print("Yes")
    else:
        print("No")


# Python program to check if a number is prime or not
def isPrime(n):
    # Corner cases
    if (n <= 1):
        return False
    if (n <= 3):
        return True
    # This is checked so that we can skip
    # middle five numbers in below loop
    if (n % 2 == 0 or n % 3 == 0):
        return False
    i = 5
    while(i * i <= n):
        if (n % i == 0 or n % (i + 2) == 0):
            return False
        i = i + 6
    return True


# Driver program to test above function
if __name__ == "__main__":
    n = 19
    if (isPrime(n)):
        print("True")
    else:
        print("False")


"""
def isPowerOfTwo(n):
    if (n == 0):
        return False
    while (n != 1):
        if (n % 2 != 0):
            return False
        n >>= 1
    return True
"""

"""
def is