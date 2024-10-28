
def comb_sort(a):
    # loop until the gap is zero
    n = len(a)
    gap = n
    swapped = True
    while gap != 0 or swapped == True:
        # set the gap and swapped to false
        gap = int(gap / 1.3)
        if gap == 0:
            gap = 1
        swapped = False
        # loop through the list
        for i in range(n - gap):
            # check if the value of the current element is greater than the next element
            if a[i] > a[i + gap]:
                # if true, then swap the two elements
                a[i], a[i + gap] = a[i + gap], a[i]
                swapped = True
    return a


