Here is a Java solution for the problem:

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

This solution calculates the total number of characters in each list by iterating over the strings in the lists and summing up the lengths. It then compares the sums and returns the list with the smaller sum. If the sums are equal, it returns the first list. 

The time complexity of this solution is O(n), where n is the total number of strings in the two lists, because it iterates over each string in the lists once. The space complexity is O(1), because it only uses a constant amount of space to store the sums and the lists. 