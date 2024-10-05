You can use Java Stream API to solve this problem. Here is a possible implementation:

```java
import java.util.*;
import java.lang.*;
import java.util.stream.Collectors;

class Solution {
    public List<Integer> removeDuplicates(List<Integer> numbers) {
        return numbers.stream()
                .filter(i -> Collections.frequency(numbers, i) == 1)
                .collect(Collectors.toList());
    }
}
```

In this implementation, we use the `stream()` method to convert the list into a stream of elements. Then, we use the `filter()` method to keep only the elements that occur exactly once in the list. Finally, we use the `collect()` method to convert the stream back into a list.

This implementation has a time complexity of O(n^2) due to the `Collections.frequency()` method being called for each element in the list. If you want to improve the performance, you can use a `HashMap` to count the occurrences of each element in the list first. Here is an improved implementation:

```java
import java.util.*;
import java.lang.*;
import java.util.stream.Collectors;

class Solution {
    public List<Integer> removeDuplicates(List<Integer> numbers) {
        Map<Integer, Integer> counts = new HashMap<>();
        for (int i : numbers) {
            counts.put(i, counts.getOrDefault(i, 0) + 1);
        }
        return numbers.stream()
                .filter(i -> counts.get(i) == 1)
                .collect(Collectors.toList());
    }
}
```

In this implementation, we use a `HashMap` to count the occurrences of each element in the list. Then, we use the same `filter()` and `collect()` methods as before to keep only the elements that occur exactly once. This implementation has a time complexity of O(n) due to the `HashMap` operations being constant time.