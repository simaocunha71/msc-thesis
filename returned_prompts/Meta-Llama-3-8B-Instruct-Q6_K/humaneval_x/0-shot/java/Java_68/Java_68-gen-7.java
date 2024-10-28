Here is a Java solution using Java 8 streams:

```java
import java.util.*;

class Solution {
    public List<Integer> pluck(List<Integer> arr) {
        return arr.stream()
                .filter(x -> x % 2 == 0)
                .min((a, b) -> Integer.compare(a, b))
                .map(x -> new ArrayList<>(Arrays.asList(x, arr.indexOf(x))))
                .orElseGet(ArrayList::new);
    }
}
```

In this solution, we first filter the array to get only the even values. Then we use the `min` method to find the smallest even value. We use the `map` method to create a new list with the smallest even value and its index. If the array is empty or does not contain any even values, the `orElseGet` method returns an empty list.

The time complexity of this solution is O(n), where n is the size of the input array, because we are iterating over the array once. The space complexity is O(1), because we are using a constant amount of space to store the result.