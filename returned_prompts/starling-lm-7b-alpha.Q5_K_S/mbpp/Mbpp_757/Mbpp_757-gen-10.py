def count_reverse_pairs(lst):
    lst_rev = []
    for s in lst:
        lst_rev.append(s[::-1])
    count = 0
    for i in range(len(lst)):
        for j in range(i+1, len(lst)):
            if lst_rev[i] == lst_rev[j]:
                count += 1
    return count

# assert count_reverse_pairs(["julia", "best", "tseb", "for", "ailuj"])== 2
# print(count_reverse_pairs(["julia", "best", "tseb", "for", "ailuj"]))

# assert count_reverse_pairs(["ab", "cd"])== 1
# print(count_reverse_pairs(["ab", "cd"]))

# assert count_reverse_pairs(["abcd", "abcd"])== 1
# print(count_reverse_pairs(["abcd", "abcd"]))

# assert count_reverse_pairs(["abcde", "abcde"])== 1
# print(count_reverse_pairs(["abcde", "abcde"]))




















"""
def count_reverse_pairs(lst):
    lst_rev = []
    for s in lst:
        lst_rev.append(s[::-1])
    count = 0
    for i in range(len(lst)):
        for j in range(i+1, len(lst)):
            if lst_rev[i] == lst_rev[j]:
                count += 1
    return count
"""

# assert count_reverse_pairs(["julia", "best", "tseb", "for", "ailuj"])== 2
# print(count_reverse_pairs(["julia", "best", "tseb", "for", "ailuj"]))

# assert count_reverse_pairs(["ab", "cd"])== 1
# print(count_reverse_p