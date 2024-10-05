```java
import java.util.*;
import java.lang.*;

class Solution {
    public List<Double> findClosestElements(List<Double> numbers) {
        if (numbers.size() < 2) {
            throw new IllegalArgumentException("List must contain at least two elements");
        }
        Collections.sort(numbers);
        double minDiff = Double.MAX_VALUE;
        List<Double> result = new ArrayList<>();
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