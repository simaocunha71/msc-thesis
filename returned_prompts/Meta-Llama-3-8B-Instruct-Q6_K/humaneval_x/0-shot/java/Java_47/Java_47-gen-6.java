Here is a Java solution using the Collections class to sort the list and then calculate the median:

```java
import java.util.*;

class Solution {
    public double median(List<Integer> l) {
        List<Integer> sortedList = new ArrayList<>(l);
        Collections.sort(sortedList);
        int n = sortedList.size();
        if (n % 2 == 0) {
            double median = (sortedList.get(n / 2 - 1) + sortedList.get(n / 2)) / 2.0;
            return median;
        } else {
            return (double) sortedList.get(n / 2);
        }
    }
}
```

This solution works by first sorting the list of integers. Then, it checks if the length of the list is even or odd. If the length is even, it calculates the median as the average of the two middle elements. If the length is odd, it simply returns the middle