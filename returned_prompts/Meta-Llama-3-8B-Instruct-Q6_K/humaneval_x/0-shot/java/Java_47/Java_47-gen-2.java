The median of a list of numbers is the middle value in the list when it is sorted in order. If the list has an even number of elements, the median is the average of the two middle values.

Here is a Java solution that calculates the median of a list of integers:

```java
import java.util.*;

class Solution {
    public double median(List<Integer> l) {
        Collections.sort(l);
        int n = l.size();
        if (n % 2 == 0) {
            return (l.get(n / 2 - 1) + l.get(n / 2)) / 2.0;
        } else {
            return l.get(n / 2);
        }
    }
}
```

This solution sorts the list of integers and then checks if the length of the list is even or odd. If the length is even, it calculates the average of the two middle values. If the length is odd, it returns the middle value. The result is a double value, which is necessary because the median of an even-length list can be a decimal number. 

This solution assumes that the input list is non-empty. If the list is empty, it will throw an exception when trying to access the first or last element. If you want to handle the empty list case, you can add a check at the beginning of the method:

```java
if (l.isEmpty()) {
    return Double.NaN; // or throw an exception, or return a default value
}
```  