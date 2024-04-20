"""
Write a python function to check whether the count of divisors is even. 
assert count_divisors(10)
"""

def count_divisors(n):
    if n==1 or n == 2:
        return False   # n = 2 is even
    
    else:
        d = []         # creating a empty list to store divisor values
            
        for i in range(2,n+1):     
            if n%i == 0:       # checking whether current value of divisors and input number are divisible or not
                d.append(i)         
    
    return len(d) % 2 == 0   # even or odd ?
