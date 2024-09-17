def catalan_number(n):
    return factorial(2*n)/(factorial(n+1)*factorial(n))
def factorial(n):
    if(n==0 or n==1):
        return 1
    else:
        return n * factorial(n-1)