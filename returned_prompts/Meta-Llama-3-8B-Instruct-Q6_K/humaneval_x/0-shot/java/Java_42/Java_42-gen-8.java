The task is to create a function that takes a list of integers as input and returns a new list with each element incremented by 1.

Here is the solution in Java:
```
import java.util.*;

class Solution {
    public List<Integer> incrList(List<Integer> l) {
        List<Integer> result = new ArrayList<>();
        for (int i : l) {
            result.add(i + 1);
        }
        return result;
    }
}
```
This function uses a for-each loop to iterate over the input list, increments each element by 1, and adds the result to a new list. The new list is then returned.

Alternatively, you can use Java 8's stream API to achieve the same result in a more concise way:
```
import java.util.*;

class Solution {
    public List<Integer> incrList(List<Integer> l) {
        return l.stream()
                .map(i -> i + 1)
                .collect(Collectors.toList());
    }
}
```
This function uses the `stream()` method to create a stream from the input list, the `map()` method to increment each element by 1, and the `collect()` method to collect the results into a new list. The new list is then returned.