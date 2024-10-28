    return sorted(arr, key=lambda x: (bin(x).count('1'), x))  # Python 3.6+
    # or
    # return sorted(arr, key=lambda x: (format(x, 'b').count('1'), x))  # Python 3.5-


