def remove_elements(l1, l2):
    for i in l2:
        while i in l1:
            l1.remove(i)
    return l1