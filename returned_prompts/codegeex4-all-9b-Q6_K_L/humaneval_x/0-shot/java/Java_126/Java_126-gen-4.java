Here is a solution using Java 8 streams:

```java
public boolean isSorted(List<Integer> lst) {
    return lst.stream()
        .distinct()
        .reduce((a, b) -> a <= b ? b : null)
        .isPresent();
}
```

This works by first removing any duplicates with the `distinct` method, then checking if the list is sorted in ascending order with `reduce`. If the list is sorted, `reduce` will return the last element in the list. If it is not sorted, `reduce` will return `null`. The `isPresent` method checks if the optional returned by `reduce` is empty, so if the list is sorted, `isSorted` will return `true`, and if it is not sorted, `isSorted` will return `false`.