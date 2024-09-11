def Find_Max_Length(a):
    max = 0
    for i in a:
        if len(i) > max:
            max = len(i)
    return max

# test
assert Find_Max_Length([[1],[1,4],[5,6,7,8]]) == 4

"""
Write a Python function to find the length of the longest sublist in a list of sublists.
The input is a list of sublists, and the output is the maximum