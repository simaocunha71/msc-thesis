def sumofFactors(n):
    sum=0
    i=1
    while i<=n:
        if(n%i==0):
            if(i%2==0):
                sum=sum+i
        i=i+1
    return sum



# Code taken from GeeksforGeeks
"""
def sum_factors(n):
    sum = 0
    i = 1
    while i <= n:
        if (n % i == 0):
            if (i % 2 == 0):
                sum = sum + i
        i = i + 1
    return sum
"""

# Driver program to test the above function
assert(sumofFactors(18)==26)
```
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
```

```

In the above code, the function sumofFactors(n) calculates the sum of even factors of a given number n. It initializes a variable sum to zero, and then starts a while loop starting from i=1. It checks if i is a factor of n (i.e., if n modulo i is zero). If it is, it checks if i is even (i.e., if i modulo 2 is zero). If i is both a factor and even, it adds i to the sum. It increments i by one and continues until i is greater than n. Finally, it returns the sum of even factors of n.

The assert statement at the end of the code checks if the function sumofFactors(18) returns the expected result of 26. If the function correctly calculates the sum of even factors of 18, the assert statement will not raise an exception and the program will execute normally. Otherwise, if the function's result is incorrect, the assert statement will raise an exception and the program will stop execution, indicating an error in the code.

This code can be used to verify the correctness of the sumofFactors function and ensure that it accurately calculates the sum of even factors of a given number.
```