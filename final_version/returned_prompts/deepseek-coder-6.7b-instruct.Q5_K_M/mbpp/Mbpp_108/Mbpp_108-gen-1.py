
def merge_sorted_list(list1, list2, list3):
    return sorted(list1 + list2 + list3)

print(merge_sorted_list([25, 24, 15, 4, 5, 29, 110],[19, 20, 11, 56, 25, 233, 154],[24, 26, 54, 48]))

"""
In the above program, we are merging three lists using "+" operator and then sorting the final list using sorted() function.
"""

# Alternative solution
def merge_sorted_list(list1, list2, list3):
    result = []
    result.extend(list1)
    result.extend(list2)
    result.extend(list3)
    return sorted(result)

print(merge_sorted_list([25, 24, 15, 4, 5, 29, 110],[19, 20, 11, 56, 25, 233, 154],[24, 26, 54, 48]))

"""
In the alternative solution, we are merging the lists using the extend() method which adds the elements of list2 and list3 to the end of list1. Then we are sorting the merged list using sorted() function.
"""

# Alternative solution
def merge_sorted_list(list1, list2, list3):
    for i in list2:
        list1.append(i)
    for i in list3:
        list1.append(i)
    return sorted(list1)

print(merge_sorted_list([25, 24, 15, 4, 5, 29, 110],[19, 20, 11, 56, 25, 233, 154],[24, 26, 54, 48]))

"""
In the alternative solution, we are directly appending list2