
def largest_smallest_integers(lst):
    pos = None
    neg = None
    for i in lst:
        if i < 0 and neg == None:
            neg = i
        elif i < 0 and neg > i:
            neg = i
        elif i > 0 and pos == None:
            pos = i
        elif i > 0 and pos < i:
            pos = i
    return (neg, pos)
