```
def count_samepair(list1, list2, list3):
    count = 0
    for i in range(len(list1)):
        if list1[i] == list2[i] == list3[i]:
            count += 1
    return count
``` 

The function count_samepair takes three lists as input and returns the count of items that are identical in the same position of the three given lists. It iterates over the elements of the lists and checks if the elements at the same position in all three lists are equal. If they are, it increments the count. Finally, it returns the count.

The unit test `assert count_samepair([1,2,3,4,5,6,7,8],[2,2,3,1,2,6,7,9],[2,1,3,1,2,6,7,9])==3` ensures that the function works correctly. It checks that the function returns 3 when the given lists have 3 identical items in the same position. 

The time complexity of this function is O(n), where n is the length of the lists. This is because it needs to iterate over all elements of the lists to find the identical items. The space complexity is O(1), as it only uses a constant amount of space to store the count and the indices. 