
def Find_Max_Length(lst):
    return max(len(sublist) for sublist in lst)

print(Find_Max_Length([[1],[1,4],[5,6,7,8]]))

"""
Here, we are using a generator expression inside the max function to iterate over all sublists in the given list and calculate their lengths. The max function then returns the length of the longest sublist.
"""

