```
def interleave_lists(list1, list2, list3):
    if len(list1) != len(list2) != len(list3):
        raise ValueError("lists must be of the same length")
    result = []
    for i in range(len(list1)):
        result.append(list1[i])
        result.append(list2[i])
        result.append(list3[i])
    return result
```


This function takes three lists as input and returns a single flat list where the elements of the input lists are interleaved. The function first checks if the lists are of the same length, and raises a ValueError if they are not. It then creates an empty list to store the result, and uses a for loop to iterate over the indices of the input lists. For each index, it appends the corresponding elements from the input lists to the result list. Finally, it returns the result list. The unit test provided ensures that the function works correctly for lists of the same length. For example, the test `assert interleave_lists([1,2,3,4,5,6,7],[10,20,30,40,50,60,70],[100,200,300,400,500,600,700])==[1, 10, 100, 2, 20, 200, 3, 30, 300, 4, 40, 400, 5, 50, 500, 6, 60, 600, 7, 70, 700]` checks that the function correctly interleaves the elements of three lists of the same length.