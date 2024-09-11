def frequency_lists(lst):
    freq = {}
    for i in lst:
        for j in i:
            if j not in freq:
                freq[j] = 1
            else:
                freq[j] += 1
    return freq


# def frequency_lists(lst):
#     freq = {}
#     for i in lst:
#         for j in i:
#             if j not in freq:
#                 freq[j] = 1
#             else:
#                 freq[j] += 1
#     return freq


def frequency_lists(lst):
    freq = {}
    for i in lst:
        for j in i:
            if j in freq:
                freq[j] += 1
            else:
                freq[j] = 1
    return freq


def frequency_lists(lst):
    freq = {}
    for i in lst:
        for j in i:
            freq.setdefault(j, 0)
            freq[j] += 1
    return freq


def frequency_lists(lst):
    freq = {}
    for i in lst:
        for j in i:
            freq[j] = freq.get(j, 0) + 1
    return freq


# def frequency_lists(lst):
#     freq = {}
#     for i in lst:
#         for j in i:
#             freq[j] = freq.get(j, 0) + 1
#     return freq

def frequency_lists(lst):
    freq = {}
    for i in lst:
        for j in i:
            freq[j] = freq.get(j, 0) + 1
    return freq


def frequency_lists(lst):
    freq = {}
    for i in lst:
        for j in i:
            freq[j] = freq.get(j, 0) + 1
    return freq


def