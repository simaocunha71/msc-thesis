def find_Rotations(str1):
    n = len(str1)
    count = 0
    for i in range(n-1):
        if str1[i] == str1[n-1]:
            count += 1
    if count == n-1:
        return 1
    else:
        return n-count