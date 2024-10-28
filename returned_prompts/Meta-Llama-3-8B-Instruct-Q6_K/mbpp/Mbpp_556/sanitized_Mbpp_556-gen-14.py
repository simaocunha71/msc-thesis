def find_Odd_Pair(lst,n):
    odd_pair_count = 0
    for i in range(n):
        for j in range(i+1,n):
            if ((lst[i] | lst[j]) % 2 != 0):
                odd_pair_count += 1
    return odd_pair_count