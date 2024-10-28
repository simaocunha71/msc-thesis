    if all(l[i] < l[i+1] for i in range(len(l)-1)):
        return True
    elif all(l[i] > l[i+1] for i in range(len(l)-1)):
        return True
    else:
        return False

