Here is the Java solution for the problem:

```java
import java.util.*;

class Solution {
    public List<String> totalMatch(List<String> lst1, List<String> lst2) {
        int sum1 = 0, sum2 = 0;
        for (String s : lst1) {
            sum1 += s.length();
        }
        for (String s : lst2) {
            sum2 += s.length();
        }
        if (sum1 < sum2) {
            return lst1;
        } else if (sum1 > sum2) {
            return lst2;
        } else {
            return lst1;
        }
    }
}
```

This solution calculates the total number of characters in each list by iterating through each string in the list and adding its length to the total. It then compares these sums and returns the list with the smaller sum. If the sums are equal, it returns the first list. 