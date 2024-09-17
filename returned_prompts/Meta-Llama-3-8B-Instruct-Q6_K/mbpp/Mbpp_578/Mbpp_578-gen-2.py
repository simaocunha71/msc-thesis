```
def interleave_lists(list1, list2, list3):
    result = []
    for i in range(len(list1)):
        result.append(list1[i])
        result.append(list2[i])
        result.append(list3[i])
    return result
```


The function interleave_lists takes three lists of the same length as input and returns a single flat list where the elements of the input lists are interleaved. The function iterates over the indices of the input lists, appending the elements of the lists at the current index to the result list. This ensures that the elements of the lists are interleaved in the correct order. The unit test provided ensures that the function works correctly for lists of length 7. 

The unit test:
```
assert interleave_lists([1,2,3,4,5,6,7],[10,20,30,40,50,60,70],[100,200,300,400,500,600,700])==[1, 10, 100, 2, 20, 200, 3, 30, 300, 4, 40, 400, 5, 50, 500, 6, 60, 600, 7, 70, 700]
```
confirms that the function correctly interleaves the input lists.  For example, the elements of the first list are interleaved with the elements of the second list, which are in turn interleaved with the elements of the third list.  The resulting list is a single flat list where the elements of the input lists are interleaved.  The function works for lists of any length, not just 7.  It is a general-purpose function for interleaving lists.  It does not modify the input lists; it returns a new list.  It raises an IndexError if the input lists are not of the same length.  It does not handle the case where the input lists are of different lengths; it is intended to be used with lists of the same length.  It is efficient in terms of memory and time; it uses a single list to store the result and it iterates over the indices of the input lists once.  It is easy to use; the user only needs to provide the input lists and the function will return the interleaved list.  It is easy to understand; the function is simple and easy to understand.  It is robust; it does not crash or produce incorrect results even if the input lists