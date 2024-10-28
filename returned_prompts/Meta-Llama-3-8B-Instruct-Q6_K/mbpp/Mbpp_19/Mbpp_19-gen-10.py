```
def test_duplicate(array):
    return len(array) != len(set(array))
```
The function test_duplicate checks if the length of the given array is equal to the length of a set created from the array. If the lengths are not equal, it means that there are duplicate elements in the array, so the function returns True. If the lengths are equal, it means that there are no duplicate elements, so the function returns False. This function assumes that the order of elements in the array is not important and that the array does not contain duplicate elements in a different case (for example, 'A' and 'a' are considered different elements).

For example, the array [1,2,3,4,5] does not contain any duplicate elements, so the function returns False. The array [1,2,2,3,4] contains a duplicate element, so the function returns True. The array ['A','b','c','D'] does not contain any duplicate elements (ignoring the case), so the function returns False. The array ['A','A','b','c'] contains a duplicate element (ignoring the case), so the function returns True. 