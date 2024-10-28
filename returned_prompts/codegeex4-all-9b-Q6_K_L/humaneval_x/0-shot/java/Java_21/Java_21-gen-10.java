```java
import java.util.*;
import java.lang.*;

class Solution {
    public List<Double> rescaleToUnit(List<Double> numbers) {
        // find min and max
        double min = numbers.stream().mapToDouble(Double::doubleValue).min().getAsDouble();
        double max = numbers.stream().mapToDouble(Double::doubleValue).max().getAsDouble();

        // rescale to unit
        List<Double> rescaled = new ArrayList<>();
        for (double num : numbers) {
            rescaled.add((num - min) / (max - min));
        }
        return rescaled;
    }
}
```