Here is the solution in Java:
```java
import java.util.*;

class Solution {
    public boolean hasCloseElements(List<Double> numbers, double threshold) {
        for (int i = 0; i < numbers.size() - 1; i++) {
            for (int j = i + 1; j < numbers.size(); j++) {
                double diff = Math.abs(numbers.get(i) - numbers.get(j));
                if (diff < threshold) {
                    return true;
                }
            }
        }
        return false;
    }
}
```
This solution iterates over all pairs of numbers in the list and checks if the absolute difference between them is less than the given threshold. If it finds such a pair, it returns `true`. If it doesn't find any such pair after checking all pairs, it returns `false`. The time complexity of this solution is O(n^2), where n is the size of the list.

For example, if you call `hasCloseElements(Arrays.asList(1.0, 2.8, 3.0, 4.0, 5.0, 2.0), 0.3)`, it will return `true` because the numbers 2.8 and 2.0 are closer than 0.3.

Note: This solution assumes that the input list is not empty. If the list can be empty, you should add a check for that at the beginning of the method. For example:
```java
public boolean hasCloseElements(List<Double> numbers, double threshold) {
    if (numbers.isEmpty()) {
        return false;
    }
    // rest of the method remains the same
}
```  