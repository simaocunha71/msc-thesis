def is_Sub_Array(l1, l2):
    for i in range(len(l2) - len(l1) + 1):
        if l2[i:i+len(l1)] == l1:
            return True
    return False