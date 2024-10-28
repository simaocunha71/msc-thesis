    The problem can be solved by iterating over the array from both ends (left and right) and comparing the elements. If the elements are not equal, we need to change one of them to make the array palindromic. We keep track of the number of elements that need to be changed.

    Here is the Java code for the solution:
```java
public int smallestChange(List<Integer> arr) {
    int left = 0;
    int right = arr.size() - 1;
    int changes = 0;
    
    while (left < right) {
        if (arr.get(left) != arr.get(right)) {
            changes++;
        }
        left++;
        right--;
    }
    return changes;
}
```
The time complexity of this solution is O(n), where n is the size of the array, because we are iterating over the array once. The space complexity is O(1), because we are using a constant amount of space to store the indices and the number of changes. 