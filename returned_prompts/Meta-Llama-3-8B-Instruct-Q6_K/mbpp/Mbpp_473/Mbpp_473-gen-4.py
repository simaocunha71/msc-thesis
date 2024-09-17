```
def tuple_intersection(tuples_list1, tuples_list2):
    set1 = set(map(tuple, tuples_list1))
    set2 = set(map(tuple, tuples_list2))
    return set(set1 & set2)
```


This function takes two lists of tuples as input. It first converts each list of tuples into a set of tuples, then finds the intersection of these two sets. The intersection operation returns a set containing all elements that are present in both sets. Since sets are unordered, the order of the tuples in the intersection set does not matter. The function returns this intersection set. 

The unit test provided ensures that the function works correctly by comparing the result of the function with the expected output. 

The function uses the built-in set and tuple functions in Python. The set function is used to convert a list into a set, and the tuple function is used to convert a list of lists into a list of tuples. The & operator is used to find the intersection of two sets. 

The time complexity of this function is O(n), where n is the total number of tuples in both input lists. This is because the function needs to iterate over each tuple in the input lists once to convert them into sets. The space complexity is also O(n), as the function needs to store the sets of tuples in memory. 