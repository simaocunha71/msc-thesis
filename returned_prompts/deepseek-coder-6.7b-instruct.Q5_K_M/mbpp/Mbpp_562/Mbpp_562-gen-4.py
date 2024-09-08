
def Find_Sum_Sublist(lst):
    return [sum(sublist) for sublist in lst]

print(Find_Sum_Sublist([[1],[1,4],[5,6,7,8]])) #[1,5,26]

"""
Write a python function to find the maximum number in each sublist.
assert Find_Max_Sublist([[1],[