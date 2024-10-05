        ArrayList<Integer> list = new ArrayList<Integer>(arr);
        Collections.sort(list, new Comparator<Integer>() {
            @Override
            public int compare(Integer o1, Integer o2) {
                int c = Integer.bitCount(o1) - Integer.bitCount(o2);
                if (c != 0) {
                    return c;
                } else {
                    return o1.compareTo(o2);
                }
            }
        });
        return list;
    }
}


A: Here is the solution you can use:
import java.util.*;

class Solution {
    public List<Integer> sortArray(List<Integer> arr) {
        return arr.stream()
                .sorted(Comparator.comparingInt(Integer::bitCount).thenComparingInt(Integer::intValue))
                .collect(Collectors.toList());
    }
}

In the solution, we are using Java 8 Streams API to sort the list. We are comparing integers based on their binary representation using bitCount() method of Integer class, and if counts are equal, then we are comparing integers based on their decimal values using intValue() method of Integer class.

A: Here is a solution using Java 8 Streams and the Comparator.comparingInt() method. It sorts the list by the number of ones in the binary representation of the numbers, and if there are ties, it sorts by the decimal value of the numbers.

```java
import java.util.Comparator;
import java.util.List;
import java.util.stream.Collectors;

public class Solution {
    public List<Integer> sortArray(List<Integer> arr) {
        return arr.stream()
                .sorted(Comparator.comparingInt(i -> Integer.bitCount(i)))
                .sorted(Comparator.comparingInt(i -> i))
                .collect(Collectors.toList());
    }
}
```

This solution works by first sorting the list by the number of ones in the binary representation of the numbers using the bitCount() method of the Integer class. If there are ties, it then sorts by the decimal value