"""
Write a python function to split a list at the nth eelment and add the first part to the end.
assert split_Arr([12,10,5,6,52,36],2) == [5,6,52,36,12,10]
"""
def split(L,n):
    assert n > 0,"enter a positive number as parameter"
    if len(L)<=n:return L
    return L[0:n]+split(L[n:],len(L)-n)