Here is the Java solution for the problem:

```java
import java.util.*;

class Solution {
    public List<Double> rescaleToUnit(List<Double> numbers) {
        if (numbers == null || numbers.size() < 2) {
            return numbers;
        }

        double min = Collections.min(numbers);
        double max = Collections.max(numbers);

        List<Double> result = new ArrayList<>();
        for (Double num : numbers) {
            result.add((num - min) / (max - min));
        }

        return result;
    }
}
```
This solution uses the built-in `Collections.min()` and `Collections.max()` methods to find the smallest and largest numbers in the list. Then, for each number in the list, it calculates the rescaled value by subtracting the smallest number and dividing by the range (i.e., the difference between the largest and smallest numbers). The result is a new list of rescaled numbers, where the smallest number is 0 and the largest is 1. 

Note: This solution assumes that the input list contains at least two elements. If the list is empty or contains only one element, the method returns the original list unchanged. If you want to handle these cases differently, you can add additional checks and handling code. 

The unit test you provided:

```java
rescaleToUnit(Arrays.asList(1.0, 2.0, 3.0, 4.0, 5.0))
```

should return:

```java
[0.0, 0.25, 0.5, 0.75, 1.0]
```

which is the expected output. 

This solution is efficient because it uses built-in methods to find the smallest and largest numbers, and it iterates over the list only once to calculate the rescaled values. The time complexity is O(n), where n is the size of the input list. The space complexity is O(n) as well, because we need to store the rescaled values in a new list. 

I hope this helps! Let me know if you have any further questions. 