
def get_pairs_count(lst, s):
    n = len(lst)
    m = [0] * 1000
    twosum = [0] * 1000
    for i in range(0, n):
        temp = s - lst[i]
        if (temp >= 0):
            twosum[temp] += 1
        m[lst[i]] += 1
    twice_count = 0
    for i in range(0, n):
        temp = s - lst[i]
        if (temp >= 0):
            twice_count += twosum[temp]
            if (temp == lst[i]):
                twice_count -= 1
    twice_count = int(twice_cut/2)
    for i in range(0, n):
        temp = s - lst[i]
        if (temp >= 0 and m[temp]):
            count += m[temp]
            if (temp == lst[i]):
                count -= 1
    return count

print(get_pairs_count([1,1,1,1],2))
"""
