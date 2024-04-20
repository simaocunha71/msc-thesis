"""
Write a function to check whether the given amount has no profit and no loss
assert noprofit_noloss(1500,1200)==False
"""
import math
def noprofit_noloss(a,b):
    # if a/b > 1 or b/a>1 return True
    
    return (a!=b and abs(a/b)>=1.5) or (abs(b/a)<=1.5) or math.isclose(1/(a+b),0,abs_tol=0.02) # not sure if this is right?
