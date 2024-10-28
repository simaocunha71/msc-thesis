```
def count_samepair(list1, list2, list3):
    count = 0
    for i in range(max(len(list1), len(list2), len(list3))):
        if i < len(list1) and i < len(list2) and i < len(list3):
            if list1[i] == list2[i] == list3[i]:
                count += 1
        elif i >= len(list1):
            if list2[i] == list3[i]:
                count += 1
        elif i >= len(list2):
            if list1[i] == list3[i]:
                count += 1
        elif i >= len(list3):
            if list1[i] == list2[i]:
                count += 1
    return count
```    
The function `count_samepair` counts the number of items that are identical in the same position of three given lists. It iterates over the maximum length of the three lists. If the item at the current position is in all three lists, it increments the count. If the item is in only two lists, it also increments the count. The function returns the total count. The unit test `assert count_samepair([1,2,3,4,5,6,7,8],[2,2,3,1,2,6,7,9],[2,1,3,1,2,6,7,9])==3` ensures the function works correctly.    
```python
assert count_samepair([1,2,3,4,5,6,7,8],[2,2,3,1,2,6,7,9],[2,1,3,1,2,6,7,9])==3
```    
This test checks that the function correctly counts the identical items in the same position of the three lists. The expected output is 3, which is the correct count of identical items.    
```python
assert count_samepair([1,2,3,4,5,6,7,8],[2,3,4,1,2,6,7,9],[2,1,3,1,2,6,7,9])==0
```    
This test checks that the function correctly counts the identical items in the same position of the three lists. The expected output is 0, which is the correct count of identical items.    
```python
assert count_samepair([1,2,