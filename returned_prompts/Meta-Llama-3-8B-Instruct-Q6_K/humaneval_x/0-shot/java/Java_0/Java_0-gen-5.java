Here is a Java solution to check if there are any two numbers in the list that are closer to each other than the given threshold.

```java
import java.util.*;

class Solution {
    public boolean hasCloseElements(List<Double> numbers, double threshold) {
        for (int i = 0; i < numbers.size(); i++) {
            for (int j = i + 1; j < numbers.size(); j++) {
                if (Math.abs(numbers.get(i) - numbers.get(j)) < threshold) {
                    return true;
                }
            }
        }
        return false;
    }
}
```

In this solution, we iterate through the list of numbers using two nested loops. For each pair of numbers, we calculate the absolute difference between them using `Math.abs(numbers.get(i) - numbers.get(j))`. If the difference is less than the threshold, we return `true`. If we don't find any pair of numbers that are closer than the threshold, we return `false`.

For example, if we call `hasCloseElements(Arrays.asList(1.0, 2.8, 3.0, 4.0, 5.0, 2.0), 0.3)`, the function will return `true` because the numbers 2.8 and 2.0 are closer than 0.3. If we call `hasCloseElements(Arrays.asList(1.0, 2.0, 3.0), 0.5)`, the function will return `false` because no two numbers in the list are closer than 0.5. 