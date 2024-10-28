def find_sum(lst):
    freq = {}
    for i in lst:
        if i in freq:
            freq[i] += 1
        else:
            freq[i] = 1
    return sum(i for i in freq if freq[i] == 1)