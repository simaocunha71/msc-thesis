def count_Substrings(s):
    n = len(s)
    count = 0
    for i in range(n):
        for j in range(i,n):
            sum = 0
            for k in range(i,j+1):
                sum += int(s[k])
            if sum == j-i+1:
                count += 1
    return count