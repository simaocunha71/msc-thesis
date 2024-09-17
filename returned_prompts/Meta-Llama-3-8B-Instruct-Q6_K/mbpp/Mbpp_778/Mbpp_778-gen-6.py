def pack_consecutive_duplicates(lst):
    result = []
    current = []
    for elem in lst:
        if not current or elem != current[-1]:
            if current:
                result.append(current)
            current = [elem]
        else:
            current.append(elem)
    if current:
        result.append(current)
    return result

assert pack_consecutive_duplicates([0, 0, 1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 8, 9, 4, 4]) == [[0, 0], [1], [2], [3], [4, 4], [5], [6, 6, 6], [7], [8], [9], [4, 4]]
print(pack_consecutive_duplicates([0, 0, 1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 8, 9, 4, 4]))


#Explanation: 
#This function iterates over the input list, maintaining a current list of consecutive duplicates.
#When a new element is encountered that is different from the last element in the current list, 
#the current list is added to the result and the current list is reset.
#At the end of the loop, the current list is added to the result if it's not empty.
#The function returns the list of lists, where each sublist contains consecutive duplicates from the input list.  # 
#This function uses a list comprehension to create the result list and a loop to iterate over the input list. 
#The time complexity is O(n), where n is the length of the input list.  # 
#The space complexity is also O(n), where n is the length of the input list, because in the worst-case scenario, 
#the function needs to store all elements of the input list in the result.  # 
#The function is tested with the given unit test, which checks if the function returns the expected result for a given input list. 
#The test passes, indicating that the function is working correctly.  # 
#The function is then called with the given input list, and the result is printed.  # 
#The output is the expected result, which is a list of lists, where each sublist contains consecutive duplicates from the input list.  # 
#The