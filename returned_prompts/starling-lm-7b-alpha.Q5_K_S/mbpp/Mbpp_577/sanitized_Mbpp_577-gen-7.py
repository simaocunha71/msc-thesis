def last_Digit_Factorial(n):
    if(n==0):
        return 1
    if(n==1):
        return 1
    if(n==2):
        return 2
    if(n==3):
        return 6
    if(n==4):
        return 4
    else:
        x=last_Digit_Factorial(n-1)
        y=last_Digit_Factorial(n-2)
        z=last_Digit_Factorial(n-3)
        return (x%10)*(y%10)*(z%10)%10