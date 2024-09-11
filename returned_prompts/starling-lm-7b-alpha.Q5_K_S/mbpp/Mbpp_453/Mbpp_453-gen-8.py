"""
def sumofFactors(n):
    sum = 0
    for i in range(1, n+1):
        if(n % i == 0):
            if(i % 2 == 0):
                sum += i
    return sum
"""

# Python program to find factors of a number
def factors(n): 
    a = [] 
    for i in range(1, n + 1): 
        if n % i == 0: 
            a.append(i) 
    return a 

def sumofFactors(n):
    sum = 0
    factorlist = factors(n)
    for i in factorlist:
        if(i % 2 == 0):
            sum += i
    return sum

# Driver program to test the above function 
print(sumofFactors(18))
"""
"""

# Python3 program to find factors of a number
def factors(n): 
    a = [] 
    for i in range(1, n + 1): 
        if n % i == 0: 
            a.append(i) 
    return a 

def sumofFactors(n):
    sum = 0
    factorlist = factors(n)
    for i in factorlist:
        if(i % 2 == 0):
            sum += i
    return sum

# Driver program to test the above function 
print(sumofFactors(18))
"""

# Python3 program to find factors of a number
def factors(n): 
    a = [] 
    for i in range(1, n + 1): 
        if n % i == 0: 
            a.append(i) 
    return a 

def sumofFactors(n):
    sum = 0
    factorlist = factors(n)
    for i in factorlist:
        if(i % 2 == 0):
            sum += i
    return sum

# Driver program to test the above function 
print(sumofFactors(18))
"""
"""

# Python3 program to find factors of a number
def factors(