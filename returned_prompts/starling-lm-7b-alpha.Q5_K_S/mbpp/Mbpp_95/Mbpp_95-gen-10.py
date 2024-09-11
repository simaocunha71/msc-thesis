def Find_Min_Length(input_list):
    """This function takes in a list of lists and returns the length of the smallest list in the list."""
    smallest_length = len(input_list[0])
    for i in range(len(input_list)):
        if len(input_list[i]) < smallest_length:
            smallest_length = len(input_list[i])
    return smallest_length

#Test Case
print(Find_Min_Length([[1],[1,2]])) #This should print 1
"""
This function works by initializing the smallest_length to the length of the first list in the input list. It then compares the length of each list in the input list with the smallest_length. If the length of the current list is less than the smallest_length, the smallest_length is updated to the length of the current list. After all lists have been compared, the smallest_length is returned.
"""

#Time Complexity: O(n) where n is the total number of elements in the input list, as we need to iterate through the lists in order to find the smallest length.
#Space Complexity: O(1) as we only need to store a single variable, the smallest_length, in order to solve the problem.

#Alternative Solution
def Find_Min_Length_Alternative(input_list):
    """This function takes in a list of lists and returns the length of the smallest list in the list."""
    return min([len(i) for i in input_list])

#Test Case
print(Find_Min_Length_Alternative([[1],[1,2]])) #This should print 1
"""
This function works by using a list comprehension to create a new list that contains the length of each list in the input list. The min function is then used to find the smallest length in this new list. This approach has the advantage of being more concise, but it may be slower for larger input lists as the min function has a time complexity of O(n).
"""

#Time Complexity: O(n) where n is the total number of elements in the input list, as we need to iterate through the lists in order to calculate the lengths.
#Space Complexity: O(n