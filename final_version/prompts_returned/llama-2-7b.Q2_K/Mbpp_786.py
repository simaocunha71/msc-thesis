"""
Write a function to locate the right insertion point for a specified value in sorted order.
assert right_insertion([1,2,4,5],6)==4
"""

def right_insertion(seq, val):
    pos=0   #starting position
    while len(seq)>pos:         #search from start of the list
        if seq[pos]<=val:  #if current value is less than or equal to the target.
            return pos+1  #update position by moving forward one element at a time
        else:                   #move forward on rightmost values only
            pos+=1                #otherwise move forwar on leftmost elements only
    return None             #when we reach end of seq, None will be returned.
