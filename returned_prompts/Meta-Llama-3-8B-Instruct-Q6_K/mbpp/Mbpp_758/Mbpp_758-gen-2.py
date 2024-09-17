```
def unique_sublists(lst):
    result = {}
    for sublist in lst:
        if isinstance(sublist, list):
            sublist = tuple(sublist)
        if sublist in result:
            result[sublist] += 1
        else:
            result[sublist] = 1
    return result
``` 
The function iterates over each element in the list. If the element is a list, it converts it to a tuple. Then it checks if the tuple is already in the result dictionary. If it is, it increments the count by 1, otherwise it adds the tuple to the dictionary with a count of 1. The function finally returns the result dictionary. 

The unit test provided ensures that the function works correctly. It checks that the function returns a dictionary where every list is converted to a tuple and the value of such tuple is the number of its occurrences in the original list. The test also checks that the function handles lists of varying lengths correctly. 

Note: This solution assumes that the input list is not empty. If the input list can be empty, the function should return an empty dictionary in this case. This can be achieved by adding a simple if statement at the beginning of the function. For example: `if not lst: return {}`. However, this is not necessary based on the provided unit test. 