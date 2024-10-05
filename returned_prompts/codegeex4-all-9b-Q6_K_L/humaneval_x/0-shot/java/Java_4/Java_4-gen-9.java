```java
import java.util.*;
import java.lang.*;

class Solution {
    public double meanAbsoluteDeviation(List<Double> numbers) {
        double sum = 0.0;
        for (Double num : numbers) {
            sum += num;
        }
        double mean = sum / numbers.size();
        double mad = 0.0;
        for (Double num : numbers) {
            mad += Math.abs(num - mean);
        }
        return mad / numbers.size();
    }
}
```
