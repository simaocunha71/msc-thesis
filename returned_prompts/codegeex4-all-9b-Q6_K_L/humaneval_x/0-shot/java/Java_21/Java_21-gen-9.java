```java
import java.util.*;
import java.lang.*;

class Solution {
    public List<Double> rescaleToUnit(List<Double> numbers) {
        double min = Double.MAX_VALUE;
        double max = Double.MIN_VALUE;

        for (double number : numbers) {
            min = Math.min(min, number);
            max = Math.max(max, number);
        }

        List<Double> result = new ArrayList<>();
        for (double number : numbers) {
            result.add((number - min) / (max - min));
        }

        return result;
    }
}
```