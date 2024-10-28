```java
import java.util.*;
import java.lang.*;

class Solution {
    public int specialFilter(List<Integer> nums) {
        return (int) nums.stream()
                .filter(n -> n > 10 && n % 2 == 1)
                .filter(n -> (n % 10) % 2 == 1)
                .count();
    }
}
```

Explanation:
1. We use the `stream()` method to convert the list to a stream.
2. We use the `filter()` method to filter out numbers that are greater than 10 and odd.
3. We use the `filter()` method again to filter out numbers whose last digit is odd.
4. We use the `count()` method to count the number of elements that meet the criteria.
5. We cast the result to an `int` and return it.