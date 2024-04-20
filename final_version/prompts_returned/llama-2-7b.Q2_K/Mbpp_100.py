"""
Write a function to find the next smallest palindrome of a specified integer, returned as an integer.
assert next_smallest_palindrome(99)==101
"""
import math

def next_smallest_palindrome(n):
    def nsp1(i):
        if i == 2:
            return 5
        else:
            ret = nsp1(int((float(i)/3.0)+1))
            # print("i:{} f:{}, rst:{}".format(str(i), str(f), str(ret)))
            if int((n/float(i)).bit_length() % 2) == n-int((n/float(i)).bit_length()):
                return ret
            else:
                raise Exception("palindrome not found")
    return nsp1(math.ceil(n/3))

# next_smallest_palindrome(99)==101
