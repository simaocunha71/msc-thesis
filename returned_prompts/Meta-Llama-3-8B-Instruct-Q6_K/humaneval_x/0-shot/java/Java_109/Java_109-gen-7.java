The problem can be solved by finding the smallest element in the array and then shifting all elements to the right until the smallest element is at the first position. If the array can be sorted in non-decreasing order by performing right shift operations, then return true; otherwise, return false.

Here is the Java code for the solution:

```java
public boolean moveOneBall(List<Integer> arr) {
    if (arr.isEmpty()) {
        return true;
    }
    int min = Collections.min(arr);
    int minIndex = arr.indexOf(min);
    if (minIndex > 0) {
        return false;
    }
    return true;
}
```

This code first checks if the array is empty. If it is, then it returns true. Otherwise, it finds the smallest element in the array using the `Collections.min` method and its index using the `indexOf` method. If the smallest element is not at the first position, then it returns false; otherwise, it returns true.

The time complexity of this solution is O(n), where n is the number of elements in the array, because the `Collections.min` and `indexOf` methods both have a time complexity of O(n). The space complexity is O(1), because it only uses a constant amount of space to store the minimum element and its index.