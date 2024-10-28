Here is the solution for the problem:

```java
import java.util.*;

class Solution {
    public List<String> totalMatch(List<String> lst1, List<String> lst2) {
        int sum1 = 0, sum2 = 0;
        for (String str : lst1) {
            sum1 += str.length();
        }
        for (String str : lst2) {
            sum2 += str.length();
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


This solution works by first calculating the total number of characters in each list. It then compares these sums to determine which list has fewer characters. If the first list has fewer characters, it returns the first list. If the second list has fewer characters, it returns the second list. If the two lists have the same number of characters, it returns the first list. This solution is O(n) time complexity where n is the total number of strings in both lists. This is because it needs to iterate over each string in both lists to calculate the total number of characters. The space complexity is O(1) as it only uses a constant amount of space to store the sums. 