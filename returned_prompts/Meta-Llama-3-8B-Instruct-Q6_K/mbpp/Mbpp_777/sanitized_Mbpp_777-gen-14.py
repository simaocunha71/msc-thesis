def find_sum(lst):
    freq = {}
    for item in lst:
        if item in freq:
            freq[item] += 1
        else:
            freq[item] = 1
    sum = 0
    for item, count in freq.items():
        if count == 1:
            sum += item
    return sum