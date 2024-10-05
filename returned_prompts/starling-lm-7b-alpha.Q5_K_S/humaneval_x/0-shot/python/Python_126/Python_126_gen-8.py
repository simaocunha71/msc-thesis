
def is_sorted(lst):
    for i in range(len(lst)-1):
        if lst[i] > lst[i+1]:
            return False
    return True



# Alternative solution
def is_sorted(lst):
    return len(set(lst)) == len(lst)



```