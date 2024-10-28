def right_insertion(lst, val):
    for i in range(len(lst)):
        if lst[i] >= val:
            return i
    return len(lst)  # or raise ValueError("val is greater than all elements in the list") if the list is not supposed to be extendable. 