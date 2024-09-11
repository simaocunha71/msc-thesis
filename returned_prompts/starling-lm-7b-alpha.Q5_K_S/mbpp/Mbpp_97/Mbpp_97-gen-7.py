def frequency_lists(lst):
    freq = {}
    for i in lst:
        for j in i:
            if j in freq:
                freq[j]+=1
            else:
                freq[j]=1
    return freq

# def frequency_lists(lst):
#     freq = {}
#     for i in lst:
#         freq.update(Counter(i))
#     return freq

# def frequency_lists(lst):
#     return {i: len(lst) - lst.count(i) for i in set(lst)}

# def frequency_lists(lst):
#     d = {}
#     for i in lst:
#         if i in d:
#             d[i]+=1
#         else:
#             d[i]=1
#     return d

# def frequency_lists(lst):
#     d = {}
#     for i in lst:
#         if i not in d:
#             d[i] = 0
#         d[i] += 1
#     return d

# def frequency_lists(lst):
#     d = {}
#     for i in lst:
#         d.update(Counter(i))
#     return d

# def frequency_lists(lst):
#     d = {}
#     for i in lst:
#         d.update(Counter(i))
#     return d

# def frequency_lists(lst):
#     d = {}
#     for i in lst:
#         d[i] = lst.count(i)
#     return d

# def frequency_lists(lst):
#     d = {}
#     for i in lst:
#         if i in d:
#             d[i]+=1
#         else:
#             d[i]=1
#     return d

# def frequency_lists(lst):
#     freq = {}
#     for i in lst:
#         if i in freq:
#             freq[i]+=1
#         else:
#             freq[i]=1
#    