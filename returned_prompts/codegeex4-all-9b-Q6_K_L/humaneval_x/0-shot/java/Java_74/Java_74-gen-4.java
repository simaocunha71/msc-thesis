```java
import java.util.*;
import java.lang.*;

class Solution {
    public List<String> totalMatch(List<String> lst1, List<String> lst2) {
        if (lst1.isEmpty() && lst2.isEmpty()) {
            return new ArrayList<>();
        }

        int sum1 = lst1.stream().mapToInt(String::length).sum();
        int sum2 = lst2.stream().mapToInt(String::length).sum();

        if (sum1 < sum2) {
            return lst1;
        } else if (sum2 < sum1) {
            return lst2;
        } else {
            return lst1;
        }
    }
}
```

This solution works by first checking if both lists are empty, in which case it returns an empty list. If not, it calculates the total number of characters in each list using the `mapToInt` and `sum` methods. It then compares the sums and returns the list with the smaller sum. If the sums are equal, it returns the first list.