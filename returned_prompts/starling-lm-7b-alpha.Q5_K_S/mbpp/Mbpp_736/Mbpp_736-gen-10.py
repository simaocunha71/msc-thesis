def left_insertion(lst,num):
    l = 0
    r = len(lst)-1
    while l<r:
        mid = (l+r)//2
        if lst[mid]>=num:
            r = mid
        else:
            l = mid+1
    return l

# assert left_insertion([1,2,4,5],6)==4
# assert left_insertion([1,2,4,5],3)==1
# assert left_insertion([],3)==0
# assert left_insertion([1,2,3],2)==0


"""
Write a function to locate the right insertion point for a specified value in sorted order.
assert right_insertion([1,2,4,5],6)==5
"""

def right_insertion(lst,num):
    l = 0
    r = len(lst)-1
    while l<r:
        mid = (l+r+1)//2
        if lst[mid]<num:
            l = mid
        else:
            r = mid-1
    return l+1

# assert right_insertion([1,2,4,5],6)==5
# assert right_insertion([1,2,4,5],3)==3
# assert right_insertion([],3)==0
# assert right_insertion([1,2,3],2)==2


"""
Write a function to insert a value into the correct position in a sorted list
assert insert_sorted([1,2,4,5],6)==[1,2,4,5,6]
"""

def insert_sorted(lst,num):
    idx = right_insertion(lst,num)
    lst.insert(idx,num)
    return lst

# assert insert_sorted([1,2,4,5],6)==[1,2,4,5,6]
# assert insert_sorted([],3)==[3]
# assert insert_sorted([1,2,3],2)==[1,2,2,3]
"""
Write a function to