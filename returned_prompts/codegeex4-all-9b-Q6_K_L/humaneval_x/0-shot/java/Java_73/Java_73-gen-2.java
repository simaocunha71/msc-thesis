Here is a Java solution that uses a two-pointer approach to solve the problem in O(n) time complexity:

```java
public int smallestChange(List<Integer> arr) {
    int i = 0, j = arr.size() - 1, changes = 0;
    while (i < j) {
        if (arr.get(i) != arr.get(j)) {
            changes++;
        }
        i++;
        j--;
    }
    return changes;
}
```

This solution works by comparing elements at the beginning and the end of the array, and moving towards the middle. If the elements are different, it increments the changes counter. This way, it counts the minimum number of changes needed to make the array palindromic.