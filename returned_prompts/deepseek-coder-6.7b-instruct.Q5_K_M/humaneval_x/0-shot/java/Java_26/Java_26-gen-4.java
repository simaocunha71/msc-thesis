        List<Integer> result = numbers.stream()
            .filter(i -> Collections.frequency(numbers, i) == 1)
            .collect(Collectors.toList());
        return result;
    }
}


A: Here's a simpler and more efficient way to do it without using Java 8 Stream API.

```java
import java.util.*;

public class Solution {

    public List<Integer> removeDuplicates(List<Integer> numbers) {
        List<Integer> result = new ArrayList<>();
        Map<Integer, Integer> map = new HashMap<>();
        
        for(Integer number : numbers) {
            if(map.containsKey(number)) {
                map.put(number, map.get(number) + 1);
            } else {
                map.put(number, 1);
            }
        }

        for(Integer number : numbers) {
            if(map.get(number) == 1) {
                result.add(number);
            }
        }
        
        return result;
    }
}
```

This solution works by first counting the occurrences of each number in the list and then adding each number to the result list if it occurs exactly once. The order of the elements in the result list is the same as the order in the input list.

Note: This solution has a time complexity of O(n), which is better than the time complexity of the Java 8 Stream API solution (O(n^2)).

Also, this solution uses extra space to store the count of each number in the list.


A: Here is an alternative solution using the Java 8 Stream API:

```java
import java.util.*;
import java.util.stream.Collectors;

public class Solution {

    public List<Integer> removeDuplicates(List<Integer> numbers) {
        Map<Integer, Long> counts = numbers.stream()
            .collect(Collectors.groupingBy(i -> i, Collectors.counting()));
        return numbers.stream()
            .filter(i -> counts.get(i) == 1)
            .collect(Collectors.toList());
    }
}
