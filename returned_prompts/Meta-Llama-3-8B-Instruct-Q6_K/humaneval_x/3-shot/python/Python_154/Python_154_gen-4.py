    return b in a or any(b in a[i:] for i in range(len(a)))  # or b in a+a


