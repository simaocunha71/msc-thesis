def last_Digit_Factorial(n):
    if n==0:
        return 1
    fact=1
    for i in range(1,n+1):
        fact*=i
    return fact%10