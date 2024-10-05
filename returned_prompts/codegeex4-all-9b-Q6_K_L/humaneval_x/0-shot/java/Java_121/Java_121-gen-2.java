Here is a Java solution that uses the Stream API to filter the list for odd numbers at even positions and then sum them up.

```java
import java.util.*;
import java.lang.*;

class Solution {
    public int solution(List<Integer> lst) {
        return lst.stream()
            .filter((num, index) -> index % 2 == 0 && num % 2 != 0)
            .mapToInt(Integer::intValue)
            .sum();
    }
}
```
This solution first creates a stream from the list, then it filters the stream to only include odd numbers at even positions. The filter method takes a BiPredicate (a function that takes two arguments and returns a boolean) where the first argument is the current number in the stream and the second argument is its index. 

The mapToInt method then transforms the stream of numbers into a stream of int, and the sum method finally calculates the sum of all the numbers in the stream. 

This solution is concise and makes good use of Java's Stream API, but it might be a bit difficult to understand at first if you're not familiar with the Stream API.