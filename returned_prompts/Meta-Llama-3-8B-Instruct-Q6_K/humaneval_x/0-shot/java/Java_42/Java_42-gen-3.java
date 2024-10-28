The problem is asking to create a function that takes a list of integers as input and returns a new list where each element is incremented by 1.

Here is the solution:
```java
import java.util.*;
import java.lang.*;
import java.util.stream.Collectors;

class Solution {
    public List<Integer> incrList(List<Integer> l) {
        return l.stream()
                 .map(i -> i + 1)
                 .collect(Collectors.toList());
    }
}
```
Explanation:

* `l.stream()` creates a stream from the input list `l`.
* `map(i -> i + 1)` applies a transformation to each element in the stream, incrementing it by 1.
* `collect(Collectors.toList())` collects the transformed elements into a new list.

You can test this function with the given examples:
```java
List<Integer> l1 = Arrays.asList(1, 2, 3);
List<Integer> result1 = new Solution().incrList(l1);
System.out.println(result1); // [2, 3, 4]

List<Integer> l2 = Arrays.asList(5, 3, 5, 2, 3, 3, 9, 0, 123);
List<Integer> result2 = new Solution().incrList(l2);
System.out.println(result2); // [6, 4, 6, 3, 4, 4, 10, 1, 124]
```
This solution uses Java 8's Stream API, which provides a concise and efficient way to process collections. The `map` function applies a transformation to each element in the stream, and the `collect` function collects the transformed elements into a new list. This approach is more readable and maintainable than a traditional loop-based solution.