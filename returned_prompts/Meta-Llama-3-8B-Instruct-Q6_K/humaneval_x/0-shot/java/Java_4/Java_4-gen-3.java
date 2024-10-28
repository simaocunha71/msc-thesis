```java
import java.util.*;

class Solution {
    public double meanAbsoluteDeviation(List<Double> numbers) {
        double mean = 0.0;
        double sum = 0.0;
        for (double num : numbers) {
            sum += num;
        }
        mean = sum / numbers.size();
        double mad = 0.0;
        for (double num : numbers) {
            mad += Math.abs(num - mean);
        }
        return mad / numbers.size();
    }
}
```
In this code, we first calculate the mean of the given list of numbers by summing up all the numbers and then dividing by the size of the list.

Then we calculate the Mean Absolute Deviation (MAD) by summing up the absolute differences between each number and the mean, and then dividing by the size of the list. The MAD is the average absolute difference between each element and the mean of this dataset.

This code assumes that the input list is not empty. If the input list is empty, it will throw an ArithmeticException when trying to divide by the size of the list. You may want to add a check for this case and return a special value (like 0.0) or throw an exception if the input list is empty. 