
def sequence(n):
    if n==0:
        return 2
    elif n==1:
        return 3
    elif n==2:
        return 5
    elif n==3:
        return 8
    elif n==4:
        return 13
    elif n>4:
        return sequence(n-1)+sequence(n-2)+sequence(n-3)
    else:
        return 0

sequence(10)
#6

"""
The Newman-Conway sequence is a sequence of numbers defined in this manner:
- The first three numbers are 2, 3, and 5.
- The nth number (for n > 3) is the sum of the (n−1)th, (n−2)th, and (n−3)rd numbers in the sequence.
"""

