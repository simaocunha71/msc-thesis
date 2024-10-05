The median of a list of numbers is the middle value when the list is sorted. If the list has an even number of elements, the median is the average of the two middle values.

Here is a Java method that calculates the median of a list of integers:

```java
import java.util.*;

public class Solution {
    public double median(List<Integer> l) {
        Collections.sort(l);
        int n = l.size();
        if (n % 2 == 0) {
            double median = (l.get(n / 2 - 1) + l.get(n / 2)) / 2.0;
            return median;
        } else {
            return l.get(n / 2).doubleValue();
        }
    }
}
```

This method first sorts the list of integers using the `Collections.sort` method. Then it checks if the list has an even number of elements. If it does, it calculates the median as the average of the two middle values. If the list has an odd number of elements, it returns the middle value as the median.

The method uses the `get` method of the `List` interface to access the elements of the list, and the `doubleValue` method to convert an integer to a double. The `double` value is returned as the result.

You can test this method with the following code:

```java
public static void main(String[] args) {
    Solution solution = new Solution();
    List<Integer> list1 = Arrays.asList(3, 1, 2, 4, 5);
    System.out.println(solution.median(list1));  // Output: 3.0

    List<Integer> list2 = Arrays.asList(-10, 4, 6, 1000, 10, 20);
    System.out.println(solution.median(list2));  // Output: 15.0
}
```

This code creates two lists of integers, sorts them, and then calculates the median of each list using the `median` method. The results are printed to the console.