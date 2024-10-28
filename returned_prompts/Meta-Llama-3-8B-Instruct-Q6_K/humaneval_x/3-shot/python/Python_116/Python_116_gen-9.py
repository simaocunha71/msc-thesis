    return sorted(arr, key=lambda x: (bin(x).count('1'), x))  # Python 3
    # return sorted(arr, key=lambda x: (bin(x).count('1'), x)) # Python 2


