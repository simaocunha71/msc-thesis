Here is a Java solution using a TreeSet to store the numbers sorted in natural order. The TreeSet allows us to quickly find the largest number smaller than a given number.

```java
import java.util.*;

class Solution {
    public List<Double> findClosestElements(List<Double> numbers) {
        // TreeSet to store the numbers sorted in natural order
        TreeSet<Double> sortedNumbers = new TreeSet<>(numbers);
        List<Double> result = new ArrayList<>();
        
        // Iterate over the numbers
        for (Double number : numbers) {
            // Find the largest number smaller than the current number
            Double next = sortedNumbers.lower(number);
            
            // If such a number exists, add it to the result
            if (next != null) {
                result.add(next);
            }
            
            // Remove the current number from the TreeSet
            sortedNumbers.remove(number);
        }
        
        // Sort the result in ascending order
        Collections.sort(result);
        
        return result;
    }
}
```

The time complexity of this solution is O(n log n), where n is the length of the input list. This is because we need to sort the list and then iterate over it. The space complexity is O(n), because we need to store the sorted list in a TreeSet.