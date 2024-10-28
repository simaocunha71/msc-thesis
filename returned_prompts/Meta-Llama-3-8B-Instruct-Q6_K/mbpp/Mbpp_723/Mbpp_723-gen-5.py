```
def count_same_pair(list1, list2):
    count = 0
    for i in range(len(list1)):
        if list1[i] == list2[i]:
            count += 1
    return count
``` 

The function `count_same_pair` takes two lists as input and returns the number of indices where the lists have the same values. It iterates over the lists and checks if the elements at the current index are equal. If they are equal, it increments the count. Finally, it returns the count. 

The unit test `assert count_same_pair([1, 2, 3, 4, 5, 6, 7, 8],[2, 2, 3, 1, 2, 6, 7, 9])==4` ensures that the function works correctly. 

This problem can be solved in O(n) time complexity, where n is the length of the lists, because it only needs to iterate over the lists once. The space complexity is O(1), which means the space required does not change with the size of the input, because it only uses a constant amount of space to store the count and the indices. 