def add_tuple(list, tuple):
    return list + tuple



"""
Write a function to remove the given element from the given list. If the element is not present in the list, the function should return the original list.

assert remove_element([1, 2, 3, 2, 1], 2) == [1, 3, 2, 1]
"""

def remove_element(list, elem):
    for i in range(len(list)):
        if list[i] == elem:
            del list[i]
            break
    return list


"""
Write a function to find the average of all elements in the given list.

assert average_list([2, 4, 6, 8]) == 5.0
"""

def average_list(list):
    return sum(list) / len(list)


"""
Write a function to find the maximum element in the given list. If the list is empty, the function should return None.

assert max_list([2, 4, 6, 8]) == 8
"""

def max_list(list):
    if len(list) == 0:
        return None
    max = list[0]
    for elem in list:
        if elem > max:
            max = elem
    return max


"""
Write a function to find the minimum element in the given list. If the list is empty, the function should return None.

assert min_list([2, 4, 6, 8]) == 2
"""

def min_list(list):
    if len(list) == 0:
        return None
    min = list[0]
    for elem in list:
        if elem < min:
            min = elem
    return min


"""
Write a function to find the maximum element in the given list of tuples, where each tuple represents a point in a plane with x and y coordinates. The x-coordinate represents the priority of a point. If there are multiple points with the same priority, the point with the higher y-coordinate should be chosen. If the list is empty, the function should return None.

assert max_tuple([(2,