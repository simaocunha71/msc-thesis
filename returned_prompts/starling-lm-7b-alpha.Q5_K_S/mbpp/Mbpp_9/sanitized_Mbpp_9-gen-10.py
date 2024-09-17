def find_Rotations(s):
    """
    Function to find the minimum number of rotations
    """
    n = len(s)
    for i in range(1,n):
        if s[:i] == s[n-i:]:
            return i
    return 0