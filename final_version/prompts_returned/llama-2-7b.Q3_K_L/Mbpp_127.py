"""
Write a function to multiply two integers.
assert multiply_int(10,20)==200
"""

def multiply_int(a,b):
    result=0 
    while b>0:
        number = a%b + a/b
        result = result * number
        a = int(number)
        b = int(b/10)
    return (result*10)+'0'
