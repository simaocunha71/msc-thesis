
def last_Digit_Factorial(n):
    if(n==0):
        return 1
    else:
        res=1
        while(n!=0):
            res*=n
            n-=1
        return res%10


