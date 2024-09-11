"""
def even_bit_set_number(n):
    i = 0
    while(n):
        if(i%2==0):
            n = n | (1<<i)
        i+=1
    return n
"""

