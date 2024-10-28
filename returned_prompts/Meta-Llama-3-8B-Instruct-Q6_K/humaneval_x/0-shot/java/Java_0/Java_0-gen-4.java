Here is the Java code that solves the problem:

```java
import java.util.*;

class Solution {
    public boolean hasCloseElements(List<Double> numbers, double threshold) {
        for (int i = 0; i < numbers.size(); i++) {
            for (int j = i + 1; j < numbers.size(); j++) {
                if (Math.abs(numbers.get(i) - numbers.get(j)) < threshold) {
                    return true;
                }
            }
        }
        return false;
    }
}
```

This code iterates over the list of numbers, comparing each number with every other number to check if any two numbers are closer to each other than the given threshold. If it finds such a pair, it returns `true`. If it doesn't find any such pair after checking all numbers, it returns `false`. 

You can test this code with the examples you provided:

```java
List<Double> list1 = Arrays.asList(1.0, 2.0, 3.0);
System.out.println(new Solution().hasCloseElements(list1, 0.5)); // prints false

List<Double> list2 = Arrays.asList(1.0, 2.8, 3.0, 4.0, 5.0, 2.0);
System.out.println(new Solution().hasCloseElements(list2, 0.3)); // prints true
```  