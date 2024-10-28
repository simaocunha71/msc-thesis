        return numbers.stream()
                .distinct()
                .collect(Collectors.toList());
    }
}


A: You can use a HashMap to count the occurrence of each number in the list. Then, you can filter the list based on the count of each number.
Here is the Java code:

```java
import java.util.*;

class Solution {
    public List<Integer> removeDuplicates(List<Integer> numbers) {
        Map<Integer, Integer> map = new HashMap<>();

        for (Integer number : numbers) {
            map.put(number, map.getOrDefault(number, 0) + 1);
        }

        List<Integer> result = new ArrayList<>();

        for (Integer number : numbers) {
            if (map.get(number) == 1) {
                result.add(number);
            }
        }

        return result;
    }
}
```

In this code, the method `removeDuplicates` takes a list of integers as input, counts the occurrence of each number in the list using a HashMap, and then creates a new list that contains only the numbers that occur exactly once. The order of the numbers in the original list is preserved in the new list.

Note: If you don't want to keep the order of the original list, you can use a LinkedHashSet instead of ArrayList in the final result.

```java
import java.util.*;

class Solution {
    public List<Integer> removeDuplicates(List<Integer> numbers) {
        Map<Integer, Integer> map = new HashMap<>();

        for (Integer number : numbers) {
            map.put(number, map.getOrDefault(number, 0) + 1);
        }

        Set<Integer> result = new LinkedHashSet<>();

        for (Integer number : numbers) {
            if (map.get(number) == 1) {
                result.add(number);
            }
        }

        return new ArrayList<>(result);
    }
}
```

This code will return a list of numbers that occur exactly once in the input list, with the order of the numbers preserved.

Note