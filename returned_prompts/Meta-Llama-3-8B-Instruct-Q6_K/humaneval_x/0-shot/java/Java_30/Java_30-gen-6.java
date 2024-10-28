Here is the solution to your problem:

```java
import java.util.*;

class Solution {
    public List<Integer> getPositive(List<Integer> l) {
        return l.stream()
                .filter(num -> num > 0)
                .collect(Collectors.toList());
    }
}
```

This solution uses Java 8's Stream API to filter the list of integers and return a new list containing only the positive numbers. The `filter` method is used to create a stream of numbers that are greater than 0, and the `collect` method is used to collect the filtered numbers into a new list. The `getPositive` method takes a list of integers as input and returns a new list containing only the positive numbers.

Here is an example usage of this method:

```java
List<Integer> numbers = Arrays.asList(-1, 2, -4, 5, 6);
List<Integer> positiveNumbers = new Solution().getPositive(numbers);
System.out.println(positiveNumbers);  // Output: [2, 5, 6]
```

This example creates a list of integers and passes it to the `getPositive` method. The method returns a new list containing only the positive numbers, which is then printed to the console. The output is a list of positive numbers: `[2, 5, 6]`.