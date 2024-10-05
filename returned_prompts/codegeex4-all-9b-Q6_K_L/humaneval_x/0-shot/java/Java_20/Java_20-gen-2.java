```java
import java.util.*;
import java.lang.*;

class Solution {
    public List<Double> findClosestElements(List<Double> numbers) {
        List<Double> result = new ArrayList<>();
        if (numbers.size() < 2) {
            return result;
        }

        // Sort the list
        Collections.sort(numbers);

        // Initialize the minimum difference to a large value
        double minDiff = Double.MAX_VALUE;

        // Iterate through the list to find the closest pair
        for (int i = 0; i < numbers.size() - 1; i++) {
            double diff = numbers.get(i + 1) - numbers.get(i);
            if (diff < minDiff) {
                minDiff = diff;
                result.clear();
                result.add(numbers.get(i));
                result.add(numbers.get(i + 1));
            }
        }

        return result;
    }
}
```