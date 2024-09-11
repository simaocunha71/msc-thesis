def noprofit_noloss(x, y):
    if(x == y):
        return True
    else:
        return False

# Python Program to check if a number is a prime
def isPrime(n):
    if (n <= 1):
        return False

    # Check from 2 to n-1
    for i in range(2, n):
