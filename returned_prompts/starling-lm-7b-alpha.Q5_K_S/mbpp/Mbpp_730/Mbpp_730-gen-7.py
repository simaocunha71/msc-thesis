def consecutive_duplicates(lst):
    new_lst = []
    for i in range(len(lst)-1):
        if lst[i] != lst[i+1]:
            new_lst.append(lst[i])
    new_lst.append(lst[-1])
    return new_lst

def test_consecutive_duplicates():
    assert consecutive_duplicates([0, 0, 1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 8, 9, 4, 4 ])==[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 4]
    print("All Tests Passed")

test_consecutive_duplicates()




"""
The function takes a list and checks if the previous element is the same as the current element. If they are the same, it ignores the current element. If they are not the same, it appends the previous element to a new list and then adds the current element to the new list. This process continues until the end of the original list is reached.

The function then returns the new list, which contains all the unique elements from the original list, except for consecutive duplicates.
"""

"""
The time complexity of this function is O(n), where n is the length of the input list. This is because the function iterates through the input list once, checking each element and deciding whether to append it to the new list or not.

The space complexity of this function is also O(n), as the new list can potentially have the same length as the input list, depending on the number of consecutive duplicates in the input list.
"""

"""
This function can be used to remove consecutive duplicates from any list, not just a list of integers. It can be used with any data type that can be compared for equality. For example, it can be used with a list of strings, a list of lists, a list of tuples, etc.
"""

"""
This function can also be modified to handle more complex cases, such as removing consecutive duplicates of a certain value, or removing consecutive duplic