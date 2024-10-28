You can use the following Java code to solve this problem:

```java
import java.util.*;

class Solution {
    public boolean hasCloseElements(List<Double> numbers, double threshold) {
        Collections.sort(numbers);
        
        for (int i = 1; i < numbers.size(); i++) {
            if (Math.abs(numbers.get(i) - numbers.get(i - 1)) < threshold) {
                return true;
            }
        }
        
        return false;
    }
}
```

This code sorts the list of numbers and then checks each pair of adjacent numbers to see if they are closer to each other than the given threshold. If it finds a pair that is closer than the threshold, it returns true. If it checks all pairs and doesn't find any that are closer than the threshold, it returns false. 

For example, if you call `hasCloseElements(Arrays.asList(1.0, 2.0, 3.0), 0.5)`, it will return false because there are no pairs of numbers that are closer than 0.5 to each other. If you call `hasCloseElements(Arrays.asList(1.0, 2.8, 3.0, 4.0, 5.0, 2.0), 0.3)`, it will return true because the numbers 2.0 and 2.8 are closer than 0.3 to each other. 

This code assumes that the input list is not null and contains at least one element. It also assumes that the threshold is a positive number. If these assumptions are not valid, you may want to add error checking code to handle these cases. 