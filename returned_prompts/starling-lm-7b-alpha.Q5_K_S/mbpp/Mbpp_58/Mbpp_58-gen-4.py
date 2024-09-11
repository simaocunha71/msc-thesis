"""
def opposite_Signs(n1,n2):
    if (n1>0 and n2<0) or (n1<0 and n2>0):
        return True
    return False
"""

# Python program to check if two numbers have opposite sign
def check_OppositeSigns(n1, n2):
    if ((n1 > 0 and n2 < 0) or (n1 < 0 and n2 > 0)):
        return True
    return False

# Driver program
if check_OppositeSigns(1, -2):
    print("True")
else:
    print("False")

# This code is contributed by PrinciRaj13
```
