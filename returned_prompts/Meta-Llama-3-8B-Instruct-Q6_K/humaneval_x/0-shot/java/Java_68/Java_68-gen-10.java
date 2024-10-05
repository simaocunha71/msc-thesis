Here is a Java solution using Java 8 Stream API:

```java
public List<Integer> pluck(List<Integer> arr) {
    return arr.stream()
            .filter(node -> node % 2 == 0)
            .min((a, b) -> Integer.compare(a, b))
            .map(node -> new ArrayList<>(Arrays.asList(node, arr.indexOf(node))))
            .orElse(new ArrayList<>());
}
```

This solution works as follows:
- It filters the list to include only even numbers using `filter(node -> node % 2 == 0)`.
- It finds the smallest even number using `min((a, b) -> Integer.compare(a, b))`.
- It maps the smallest even number to a list containing the number and its index in the original list using `map(node -> new ArrayList<>(Arrays.asList(node, arr.indexOf(node))))`.
- If the list is empty or there are no even numbers, it returns an empty list using `orElse(new ArrayList<>())`.
- Finally, it returns the result as a list. 

This solution has a time complexity of O(n log n) due to the `min` operation, where n is the size of the input list. The space complexity is O(n) due to the creation of the result list.  Q.E.D. 