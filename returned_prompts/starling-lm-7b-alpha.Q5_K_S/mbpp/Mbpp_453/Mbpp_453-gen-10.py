"""
def sumofFactors(n):
    if n%2 == 0:
        return (n//2)*(n+1)
    else:
        return (n//2)*(n+1)-n

def sumofFactors(n):
    sum = 0
    for i in range(2,n):
        if n%i == 0:
            if i%2 == 0:
                sum = sum+i
    return sum
"""

