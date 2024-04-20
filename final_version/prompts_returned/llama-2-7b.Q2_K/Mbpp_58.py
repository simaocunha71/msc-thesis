"""
Write a python function to check whether the given two integers have opposite sign or not.
assert opposite_Signs(1,-2) == True
"""
import math

def opposite_Signs(a,b):
    if not isinstance(a,int) or not isinstance(b,int):
        return None
    
    # Check sign of a and b.
    sign_of_a = -1 if a < 0 else 1;
    sign_of_b = -1 if b < 0 else 1;

    if sign_of_a == sign_of_b: return False;
    
    return True;

if __name__=="__main__":
    print(opposite_Signs(4,-7))
