```
def interleave_lists(list1, list2, list3):
    result = []
    for i in range(len(list1)):
        result.append(list1[i])
        result.append(list2[i])
        result.append(list3[i])
    return result
```
The problem is asking to create a function that takes three lists of the same length and returns a single list where the elements from each of the input lists are interleaved. For example, if the input lists are `[1,2,3,4,5,6,7]`, `[10,20,30,40,50,60,70]`, and `[100,200,300,400,500,600,700]`, the output should be `[1, 10, 100, 2, 20, 200, 3, 30, 300, 4, 40, 400, 5, 50, 500, 6, 60, 600, 7, 70, 700]`.

The unit test `assert interleave_lists([1,2,3,4,5,6,7],[10,20,30,40,50,60,70],[100,200,300,400,500,600,700])==[1, 10, 100, 2, 20, 200, 3, 30, 300, 4, 40, 400, 5, 50, 500, 6, 60, 600, 7, 70, 700]` helps to clarify the expected behavior of the function.

Here is a Python solution that uses a for loop to iterate over the indices of the input lists and appends the corresponding elements from each list to the result list:
```
def interleave_lists(list1, list2, list3):
    result = []
    for i in range(len(list1)):
        result.append(list1[i])
        result.append(list2[i])
        result.append(list3[i])
    return result
```



The function `interleave_lists` takes three lists as input and returns a new list that is the interleaved result of the input lists. The function uses a for loop to iterate over the indices of the input lists, and for each index, it appends the corresponding elements from each list to the result list. The result list is then returned.

For example, if the input lists are `[1,2,3,