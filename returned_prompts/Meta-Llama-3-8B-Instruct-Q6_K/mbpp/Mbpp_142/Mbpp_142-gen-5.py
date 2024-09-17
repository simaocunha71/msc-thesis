```
def count_samepair(list1, list2, list3):
    count = 0
    for i in range(max(len(list1), len(list2), len(list3))):
        if i < len(list1) and i < len(list2) and i < len(list3):
            if list1[i] == list2[i] == list3[i]:
                count += 1
    return count
```


The provided unit test `assert count_samepair([1,2,3,4,5,6,7,8],[2,2,3,1,2,6,7,9],[2,1,3,1,2,6,7,9])==3` suggests that the function should count the number of items that are identical in the same position of three given lists. This can be achieved by iterating over the maximum length of the three lists and checking if the elements at the same position are equal. If they are, increment the count. Finally, return the count. 





Note: The unit test provided ensures that the function works correctly, and the function is designed to pass this test.