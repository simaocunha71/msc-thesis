def issort_list(lst):
    return all(lst[i] <= lst[i + 1] for i in range(len(lst) - 1))

print(issort_list([1,2,4,6,8,10,12,14,16,17]))

