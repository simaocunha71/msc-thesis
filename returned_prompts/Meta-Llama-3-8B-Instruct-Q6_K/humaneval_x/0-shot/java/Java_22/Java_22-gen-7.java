```java
import java.util.*;

class Solution {
    public List<Integer> filterIntergers(List<Object> values) {
        List<Integer> integers = new ArrayList<>();
        for (Object value : values) {
            if (value instanceof Integer) {
                integers.add((Integer) value);
            }
        }
        return integers;
    }
}
```
Explanation:
This Java code defines a method `filterIntergers` that takes a list of objects as input and returns a list of integers. The method iterates over the input list using a for-each loop, and for each object, it checks if the object is an instance of `Integer` using the `instanceof` operator. If the object is an `Integer`, it adds the `Integer` to a new list `integers`. Finally, the method returns the list of integers.

The test cases provided in the problem statement demonstrate the expected behavior of the method. For example, the test case `filter_integers(Arrays.asList('a', 3.14, 5))` expects the output `[5]` because `5` is the only integer in the input list, and the test case `filter_integers(Arrays.asList(1, 2, 3, "abc", Map.of(), List.of()))` expects the output `[1, 2, 3]` because `1`, `2`, and `3` are the only integers in the input list.