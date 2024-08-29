
def count_Pairs(lst, n):
    count = 0
    for i in range(n):
        for j in range(i+1, n):
            if lst[i] != lst[j]:
                count += 1
    return count

print(count_Pairs([1,2,1],3))


