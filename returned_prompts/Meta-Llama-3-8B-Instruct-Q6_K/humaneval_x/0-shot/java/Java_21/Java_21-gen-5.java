Here is a simple and efficient solution in Java:

```java
import java.util.*;

class Solution {
    public List<Double> rescaleToUnit(List<Double> numbers) {
        if (numbers == null || numbers.size() < 2) {
            return numbers;
        }

        double min = Collections.min(numbers);
        double max = Collections.max(numbers);

        if (max == min) {
            return numbers;
        }

        List<Double> result = new ArrayList<>();
        for (double num : numbers) {
            result.add((num - min) / (max - min));
        }

        return result;
    }
}
```

This solution first calculates the minimum and maximum values in the input list. If the minimum and maximum values are the same, it returns the original list. Otherwise, it iterates over the list, subtracts the minimum value from each number and divides the result by the difference between the maximum and minimum values. The result is a new list where the smallest number is 0 and the largest is 1. The time complexity is O(n), where n is the size of the input list, and the space complexity is also O(n) for the result list.