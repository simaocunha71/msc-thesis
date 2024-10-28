```
def count_Occurrence(tup, elements):
    return sum(1 for x in tup if x in elements)
```
This function counts the occurrence of all elements in the list in the tuple. The function uses a generator expression to iterate over each element in the tuple and checks if the element is in the list of elements to count. It then sums up the count of each element. 

The unit test provided, `assert count_Occurrence(('a', 'a', 'c', 'b', 'd'),['a', 'b'] ) == 3`, shows that the function should return 3, which is the count of 'a' in the tuple. 

This function will return the total count of all elements in the list that are present in the tuple. If you want to count the occurrence of each element separately, you would need to use a dictionary to store the count of each element. 

Here is an example of how you could do that:
```
def count_Occurrence(tup, elements):
    count_dict = {}
    for x in tup:
        if x in elements:
            if x in count_dict:
                count_dict[x] += 1
            else:
                count_dict[x] = 1
    return count_dict
```
This function will return a dictionary where the keys are the elements in the list and the values are the count of each element in the tuple. 

Note: This function is case sensitive and will not count elements that are in a different case. For example, 'a' and 'A' will be counted as different elements. If you want to count elements in a case insensitive manner, you can convert the tuple and the list to lower case or upper case before counting. 

Here is an example of how you could do that:
```
def count_Occurrence(tup, elements):
    tup = [x.lower() for x in tup]
    elements = [x.lower() for x in elements]
    count_dict = {}
    for x in tup:
        if x in elements:
            if x in count_dict:
                count_dict[x] += 1
            else:
                count_dict[x] = 1
    return count_dict
```
This function will convert the tuple and the list to lower case before counting, so 'a' and 'A' will be counted as the same element. 