```
def div_list(list1, list2):
    if len(list1) != len(list2):
        return "Lists must be of the same length"
    return [x/y for x, y in zip(list1, list2)]
```


This function takes two lists as input, checks if they are of the same length, and then uses a list comprehension to divide each element of the first list by the corresponding element of the second list. The zip function is used to pair up the elements of the two lists. If the lists are not of the same length, the function returns an error message. The unit test `assert div_list([4,5,6],[1, 2, 3])==[4.0,2.5,2.0]` ensures that the function works correctly. The division operation is floating point division, so the result will be a list of floating point numbers even if the inputs are integers.  This can be changed to integer division by using the // operator instead of /.
```
def div_list(list1, list2):
    if len(list1) != len(list2):
        return "Lists must be of the same length"
    return [x//y for x, y in zip(list1, list2)]
```
However, this will return integer division results, so if the division result is a float, it will be truncated. For example, 5//2 will return 2, not 2.5. If you want to keep the decimal part of the result, you should use the / operator instead of //.
```
def div_list(list1, list2):
    if len(list1) != len(list2):
        return "Lists must be of the same length"
    return [x/y for x, y in zip(list1, list2)]
```  This will return the decimal part of the result, so 5/2 will return 2.5.  If you want to avoid division by zero, you should add a check to make sure that the elements of list2 are not zero before performing the division.  For example:
```
def div_list(list1, list2):
    if len(list1) != len(list2):
        return "Lists must be of the same length"
    return [x/y if y != 0 else None for x, y in zip(list1, list2)]
```  This will return None for any element in list2 that is zero, to avoid division