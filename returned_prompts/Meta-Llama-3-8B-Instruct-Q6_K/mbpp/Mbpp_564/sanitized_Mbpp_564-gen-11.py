def count_Pairs(lst, n):
    seen = set()
    count = 0
    for i in range(n):
        for j in range(i+1, n):
            if lst[i] not in seen and lst[j] not in seen and lst[i] != lst[j]:
                count += 1
                seen.add(lst[i])
                seen.add(lst[j])
    return count