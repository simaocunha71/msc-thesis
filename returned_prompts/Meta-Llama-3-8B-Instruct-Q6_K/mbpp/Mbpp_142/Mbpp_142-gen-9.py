```
def count_samepair(list1, list2, list3):
    count = 0
    for i in range(len(list1)):
        if list1[i] == list2[i] == list3[i]:
            count += 1
    return count
```


The function takes in three lists and returns the count of items that are identical in the same position of the three given lists. It iterates over each position in the lists and checks if the items at that position are equal. If they are, it increments the count. Finally, it returns the count. This is a simple and efficient solution for this problem. The unit test provided in the question can be used to verify that this function works correctly. For example, the test `assert count_samepair([1,2,3,4,5,6,7,8],[2,2,3,1,2,6,7,9],[2,1,3,1,2,6,7,9])==3` checks that the function correctly counts the number of identical items in the same position of the three lists. 





The unit test provided in the question is:

```
assert count_samepair([1,2,3,4,5,6,7,8],[2,2,3,1,2,6,7,9],[2,1,3,1,2,6,7,9])==3
```

This test checks that the function correctly counts the number of identical items in the same position of the three lists. In this case, the function should return 3 because the items at positions 1, 2, and 5 are identical in all three lists. The function can be tested with this unit test to ensure that it is working correctly.