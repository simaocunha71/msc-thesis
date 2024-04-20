"""
Write a python function to count the number of set bits (binary digits with value 1) in a given number.
assert count_Set_Bits(2) == 1
"""
#!/bin/python3

def count_setbits(n, k=0):
    """
     :param n: input_number to be checked for its set bits
     :return: return number of set bits in given number
    """
    # your code goes here
    ans = 0
    while(k<32):
        if (n&1)!=0:
            k+=1
            ans+=1
        n>>=1
        
    return ans