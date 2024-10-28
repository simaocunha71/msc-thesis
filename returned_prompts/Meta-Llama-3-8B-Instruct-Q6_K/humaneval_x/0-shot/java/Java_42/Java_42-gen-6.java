```java
import java.util.*;
import java.util.stream.Collectors;

public class Solution {
    public List<Integer> incrList(List<Integer> l) {
        return l.stream().map(i -> i + 1).collect(Collectors.toList());
    }
}
```
Explanation:
The problem asks to create a function that takes a list of integers as input and returns a new list where each element is incremented by 1.

In this solution, we use the Java Stream API to achieve this. We use the `stream()` method to convert the input list into a stream, then use the `map()` method to apply a transformation to each element in the stream. In this case, we add 1 to each element. Finally, we use the `collect()` method to collect the resulting stream into a new list.

The resulting list is then returned by the `incrList()` method.

Example usage:
```java
List<Integer> inputList = Arrays.asList(1, 2, 3);
List<Integer> result = new Solution().incrList(inputList);
System.out.println(result); // Output: [2, 3, 4]
``` 