def last_Digit_Factorial(n):
    if n<=1:
        return 1
    else:
        return (n * last_Digit_Factorial(n-1))%10

print(last_Digit_Factorial(4))

#Output: 4

#Explanation: 
#The factorial of 4 is 4*3*2*1 = 24. The last digit of 24 is 4, so the function should return 4.

#Note: 
#The function uses recursion to find the factorial, and then uses modulo 10 to find the last digit.
<jupyter_output>
4
<jupyter_text>
Q2:
<jupyter_code>
