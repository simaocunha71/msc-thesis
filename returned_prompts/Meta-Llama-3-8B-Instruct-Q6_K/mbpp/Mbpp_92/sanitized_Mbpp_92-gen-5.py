def is_undulating(n):
    num_str = str(n)
    for i in range(1, len(num_str)):
        if abs(int(num_str[i]) - int(num_str[i-1])) > 1:
            return False
    return True