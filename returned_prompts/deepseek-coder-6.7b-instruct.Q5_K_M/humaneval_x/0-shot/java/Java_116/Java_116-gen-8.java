        // Your code here
    }
}

The answer:
```java
import java.util.*;
import java.lang.*;

class Solution {
    public List<Integer> sortArray(List<Integer> arr) {
        return arr.stream()
                .sorted(Comparator.comparing(i -> Integer.bitCount(i))
                        .thenComparingInt(i -> i))
                .collect(Collectors.toList());
    }
}
```

The bitCount() function is used to count the number of one's in binary representation of the number. Then it compares the count of ones. If counts are equal, then it compares the decimal values of the numbers. The sorted() function sorts the stream in ascending order based on the comparator.

The sorted() function also uses the thenComparingInt() function to compare the numbers in case of a tie in the count of ones.

Finally, the collect() function is used to convert the stream back into a List.

This solution has a time complexity of O(n log n) because of the sorting operation, where n is the size of the input list.

It's a bit tricky to understand but if you understand the idea of Comparator in Java, it will be quite easy to understand this solution.

Also, make sure to import the required packages (java.util.stream, java.util.Comparator, java.util.stream.Collectors) in order to use the methods provided by them.

Hope this helps.
```




































































































































































