Here is the solution in Java:

```java
import java.util.*;

class Solution {
    public boolean hasCloseElements(List<Double> numbers, double threshold) {
        numbers.sort((a, b) -> Double.compare(a, b));
        for (int i = 1; i < numbers.size(); i++) {
            if (Math.abs(numbers.get(i) - numbers.get(i - 1)) < threshold) {
                return true;
            }
        }
        return false;
    }
}
```

Explanation:
The function takes a list of double numbers and a threshold as input. It first sorts the list in ascending order. Then it iterates over the list, checking if the absolute difference between each pair of adjacent numbers is less than the threshold. If it finds such a pair, it returns `true`. If it doesn't find any such pair after checking all numbers, it returns `false`.

In the example you provided, the list `Arrays.asList(1.0, 2.8, 3.0, 4.0, 5.0, 2.0)` has two adjacent numbers (2.0 and 2.8) that are closer to each other than the threshold 0.3, so the function returns `true`. The list `Arrays.asList(1.0, 2.0, 3.0)` doesn't have any adjacent numbers that are closer to each other than the threshold 0.5, so the function returns `false`.