"""
Write a python function to count the number of positive numbers in a list.
assert pos_count([1,-2,3,-4]) == 2
"""
import math

def pos_count(nums):
    n=0 #count the number of positive integers
    
    for i,x in enumerate(nums):
        if x>0:
            n+=1
            
    return n

if __name__=="__main__":
    print('Enter a list : '+str(input())+' and press enter')
    print(pos_count([int(i) for i in input()]))