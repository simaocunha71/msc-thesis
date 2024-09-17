
import math
def find_Index(n):
    i = 1
    while True:
        triangular_num = i*(i+1)//2
        if len(str(triangular_num)) == n:
            return i
        i += 1
"""
This function works by generating triangular numbers in a while loop. It keeps track of the number of iterations in the loop (i) and checks if the number of digits in the current triangular number equals n. If it does, the function returns the current index. If not, the function increments the index and continues.
"""

