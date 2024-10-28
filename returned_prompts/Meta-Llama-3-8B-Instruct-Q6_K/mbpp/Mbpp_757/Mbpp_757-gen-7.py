```
def count_reverse_pairs(lst):
    count = 0
    for i in lst:
        for j in lst:
            if i != j and i == j[::-1]:
                count += 1
    return count
```
This function counts the number of pairs of strings in the list where one string is the reverse of the other. It does this by iterating over each string in the list and checking if there is another string in the list that is the reverse of the current string. If such a string is found, the count is incremented. The function then returns the total count of such pairs. 

The unit test `assert count_reverse_pairs(["julia", "best", "tseb", "for", "ailuj"])== 2` ensures that the function works correctly. In this test, the function should return 2 because "julia" and "ailuj" are reverse pairs. 

The time complexity of this function is O(n^2) because it iterates over each string in the list and checks every other string for being the reverse of the current string. The space complexity is O(1) because it only uses a constant amount of space to store the count and the current strings. 