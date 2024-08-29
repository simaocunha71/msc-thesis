def min_of_three(a,b,c):
    if a<=b and a<=c:
        return a
    elif b<=a and b<=c:
        return b
    else:
        return c

assert min_of_three(10,20,0)==0
assert min_of_three(100,50,25)==25
assert min_of_three(1,1,1)==1
assert min_of_three(0,-1,-2)==-2
assert min_of_three(-5,-10,-15)==-15
print("All tests passed")

