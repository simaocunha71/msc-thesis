```java
import java.util.*;
import java.lang.*;

class Solution {
    public double meanAbsoluteDeviation(List<Double> numbers) {
        if (numbers.size() == 0) {
            return 0;
        }
        double mean = 0;
        for (double num : numbers) {
            mean += num;
        }
        mean /= numbers.size();
        double mad = 0;
        for (double num : numbers) {
            mad += Math.abs(num - mean);
        }
        mad /= numbers.size();
        return mad;
    }
}
```