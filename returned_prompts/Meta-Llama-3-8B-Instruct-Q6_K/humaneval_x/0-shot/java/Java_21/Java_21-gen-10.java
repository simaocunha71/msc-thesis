Here is a Java solution for the problem. The idea is to find the minimum and maximum values in the list, then subtract the minimum and divide by the range to rescale the values to the range [0, 1].

```java
import java.util.*;

class Solution {
    public List<Double> rescaleToUnit(List<Double> numbers) {
        if (numbers.size() < 2) {
            return numbers;
        }

        double min = Collections.min(numbers);
        double max = Collections.max(numbers);

        List<Double> result = new ArrayList<>();
        for (double num : numbers) {
            result.add((num - min) / (max - min));
        }

        return result;
    }
}
```

This solution has a time complexity of O(n), where n is the size of the input list, as it needs to iterate over the list twice (once to find the minimum and maximum, and once to rescale the values). The space complexity is O(n) as it needs to store the result in a new list. 

You can test this solution with the following code:

```java
public static void main(String[] args) {
    Solution solution = new Solution();
    List<Double> numbers = Arrays.asList(1.0, 2.0, 3.0, 4.0, 5.0);
    List<Double> result = solution.rescaleToUnit(numbers);
    System.out.println(result);
}
```

This will output:

```
[0.0, 0.25, 0.5, 0.75, 1.0]
```

Which is the expected result. 

This solution works for any list of numbers, not just integers. The `Collections.min` and `Collections.max` methods return the smallest and largest values in the list, regardless of their types. The rescaling is done using the formula `(num - min) / (max - min)`, which maps the range of the original values to the range [0, 1]. 

Note that this solution assumes that the input list is not empty and contains at least two elements. If the input list can be empty or contain only one element, you should add error checking code to handle these cases. 

Also, this solution returns a new list, it does not modify the original list. If you want to modify the original list, you can use a loop to rescale the values in place. 

Finally, this solution uses the `ArrayList` class to store the result