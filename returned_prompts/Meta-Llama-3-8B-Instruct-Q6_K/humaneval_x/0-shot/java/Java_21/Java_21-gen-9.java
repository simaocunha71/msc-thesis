Here is the solution in Java:
```java
import java.util.*;

class Solution {
    public List<Double> rescaleToUnit(List<Double> numbers) {
        if (numbers.size() < 2) {
            return numbers;
        }

        double min = Collections.min(numbers);
        double max = Collections.max(numbers);

        List<Double> rescaled = new ArrayList<>();
        for (double num : numbers) {
            rescaled.add((num - min) / (max - min));
        }

        return rescaled;
    }
}
```
The solution uses the `Collections.min()` and `Collections.max()` methods to find the smallest and largest numbers in the list. It then uses a for-each loop to iterate over the list, subtracting the smallest number from each number and then dividing the result by the range of the original numbers (i.e., the difference between the largest and smallest numbers). The resulting list is returned. If the input list has fewer than two elements, the original list is returned unchanged.