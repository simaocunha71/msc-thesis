```java
import java.util.*;
import java.lang.*;

class Solution {
    public List<Double> findClosestElements(List<Double> numbers) {
        Collections.sort(numbers);
        double minDiff = Double.MAX_VALUE;
        List<Double> closestElements = new ArrayList<>();
        for (int i = 0; i < numbers.size() - 1; i++) {
            double diff = numbers.get(i + 1) - numbers.get(i);
            if (diff < minDiff) {
                minDiff = diff;
                closestElements.clear();
                closestElements.add(numbers.get(i));
                closestElements.add(numbers.get(i + 1));
            }
        }
        return closestElements;
    }
}
```