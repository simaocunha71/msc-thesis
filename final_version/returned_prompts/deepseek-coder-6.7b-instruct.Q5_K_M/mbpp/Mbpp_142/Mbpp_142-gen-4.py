def difference_in_lengths(lst):
    return max(len(x) for x in lst) - min(len(x) for x in lst)

print(difference_in_lengths(["hello","world","python","programming"]))

"""
Here, the function calculates the maximum and minimum lengths of strings in the list.