def find_sum(lst):
    from collections import Counter
    count = Counter(lst)
    return sum(i for i in lst if count[i] == 1)  # sum of non-repeated elements