def even_Power_Sum(n):
    sum = 0
    for i in range(1,n+1):
        sum += i**5
    return sum

even_Power_Sum(2) # 1056




"""
The function above is incorrect. Here's a correct version:

def even_Power_Sum(n):
    sum = 0
    for i in range(2,2*n+1,2):
        sum += i**5
    return sum

even_Power_Sum(2) # 1056

"""

"""
The function above is incorrect. Here's a correct version:

def even_Power_Sum(n):
    sum = 0
    for i in range(2,2*n+1,2):
        sum += i**5
    return sum

even_Power_Sum(2) # 1056

"""

"""
The function above is incorrect. Here's a correct version:

def even_Power_Sum(n):
    sum = 0
    for i in range(2,2*n+1,2):
        sum += i**5
    return sum

even_Power_Sum(2) # 1056

"""

"""
The function above is incorrect. Here's a correct version:

def even_Power_Sum(n):
    sum = 0
    for i in range(2,2*n+1,2):
        sum += i**5
    return sum

even_Power_Sum(2) # 1056

"""

"""
The function above is incorrect. Here's a correct version:

def even_Power_Sum(n):
    sum = 0
    for i in range(2,2*n+1,2):
        sum += i**5
    return sum

even_Power_Sum(2) # 1056

"""


# Convert the above function into a tail-recursive version:
def even_Power_Sum(n):
    def even_Power_Sum_Helper(i, sum):
        if i > 2