You can solve this problem by iterating through the list and checking if the difference between any two adjacent elements is less than the given threshold. Here is the Java code to do this:

```java
import java.util.*;

class Solution {
    public boolean hasCloseElements(List<Double> numbers, double threshold) {
        for (int i = 1; i < numbers.size(); i++) {
            if (Math.abs(numbers.get(i) - numbers.get(i - 1)) < threshold) {
                return true;
            }
        }
        return false;
    }
}
```

This code iterates through the list using a for loop, starting from the second element (index 1). For each element, it calculates the absolute difference with the previous element using `Math.abs(numbers.get(i) - numbers.get(i - 1))`. If this difference is less than the given threshold, it returns `true`. If it checks all elements without finding any pair of elements that are closer than the threshold, it returns `false`. 

You can test this code with the examples you provided:

```java
List<Double> numbers1 = Arrays.asList(1.0, 2.0, 3.0);
System.out.println(new Solution().hasCloseElements(numbers1, 0.5)); // prints false

List<Double> numbers2 = Arrays.asList(1.0, 2.8, 3.0, 4.0, 5.0, 2.0);
System.out.println(new Solution().hasCloseElements(numbers2, 0.3)); // prints true
``` 