```
def count_samepair(list1, list2, list3):
    count = 0
    for i in range(min(len(list1), len(list2), len(list3))):
        if list1[i] == list2[i] == list3[i]:
            count += 1
    return count
```


The function count_samepair takes three lists as input and returns the number of items that are identical in the same position of the three given lists. It iterates over the lists and checks if the items at the same index are equal. If they are, it increments the count. The function returns the count at the end. The unit test `assert count_samepair([1,2,3,4,5,6,7,8],[2,2,3,1,2,6,7,9],[2,1,3,1,2,6,7,9])==3` shows that the function should return 3, which is the number of identical items in the same position. 