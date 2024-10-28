```java
import java.util.*;

public class Main {
    public static void main(String[] args) {
        List<Double> numbers = Arrays.asList(1.0, 2.0, 3.0, 4.0);
        double mad = meanAbsoluteDeviation(numbers);
        System.out.println(mad);
    }

    public static double meanAbsoluteDeviation(List<Double> numbers) {
        double mean = 0;
        double sum = 0;
        for (double num : numbers) {
            sum += num;
        }
        mean = sum / numbers.size();
        double mad = 0;
        for (double num : numbers) {
            mad += Math.abs(num - mean);
        }
        return mad / numbers.size();
    }
}
```
The function `meanAbsoluteDeviation` takes a list of numbers as input, calculates the mean of the list, and then calculates the absolute deviation of each number from the mean. The mean absolute deviation is then calculated by averaging the absolute deviations. This is done by summing up the absolute deviations and dividing by the number of elements in the list. The result is returned as a double value.

In the main function, we create a list of numbers, call the `meanAbsoluteDeviation` function, and print the result. The output is `1.0`, which is the mean absolute deviation of the input list.