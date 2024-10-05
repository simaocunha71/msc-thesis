Here's the Java implementation:

```java
import java.util.*;
import java.lang.*;

class Solution {
    public List<Integer> rollingMax(List<Integer> numbers) {
        List<Integer> result = new ArrayList<>();
        int max = Integer.MIN_VALUE;

        for (int number : numbers) {
            max = Math.max(max, number);
            result.add(max);
        }

        return result;
    }

    public static void main(String[] args) {
        Solution solution = new Solution();
        List<Integer> numbers = Arrays.asList(1, 2, 3, 2, 3, 4, 2);
        System.out.println(solution.rollingMax(numbers));
    }
}
```

The `rollingMax` method takes a list of integers as input and returns a new list containing the rolling maximum of the input list. It initializes a variable `max` to `Integer.MIN_VALUE`, which represents the minimum possible integer value in Java. 

Then, it iterates through the input list and updates the `max` value with the maximum of the current number and the current `max` value. It also adds the `max` value to the result list. 

Finally, it returns the result list. 

In the `main` method, we create an instance of the `Solution` class and call the `rollingMax` method with a sample input list. We then print the result to the console. 

This implementation has a time complexity of O(n), where n is the size of the input list.