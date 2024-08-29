def find_Max_Num(lst):
    lst.sort(reverse=True)
    return int("".join(map(str, lst)))

print(find_Max_Num([1,2,3]))  # 321

"""
Explanation:
The function takes a list of digits as input. The list is sorted in reverse order so that the largest number can be formed. The numbers are then joined together using the join() function and converted back into integers using int().
"""

# 2.
