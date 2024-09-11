from collections import Counter
def two_unique_nums(lst):
    count = Counter(lst)
    return [num for num, freq in count.items() if freq == 1]
    # return [num for num in set(lst) if lst.count(num) == 1] # alternative solution
    # return sorted(set(lst)) # alternative solution, but not guaranteed to be in the same order as the original list
    # return [num for num in lst if lst.count(num) == 1] # alternative solution, but not efficient for large lists