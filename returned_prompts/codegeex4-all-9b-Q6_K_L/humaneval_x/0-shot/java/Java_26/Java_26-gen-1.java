Here is a Java solution using Java 8 streams:

```java
import java.util.*;
import java.util.stream.Collectors;

class Solution {
    public List<Integer> removeDuplicates(List<Integer> numbers) {
        return numbers.stream()
                      .distinct()
                      .collect(Collectors.toList());
    }

    public static void main(String[] args) {
        Solution solution = new Solution();
        List<Integer> numbers = Arrays.asList(1, 2, 3, 2, 4);
        System.out.println(solution.removeDuplicates(numbers));  // [1, 3, 4]
    }
}
```

Explanation:
- `numbers.stream()` converts the list into a stream.
- `distinct()` removes duplicate elements from the stream.
- `collect(Collectors.toList())` converts the stream back into a list.