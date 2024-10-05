Here is the solution in Java:
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
This solution calculates the total number of characters in each list and compares them. If the total number of characters in the first list is less than the second list, it returns the first list. If the total number of characters in the second list is less than the first list, it returns the second list. If the total number of characters in both lists is the same, it returns the first list. This solution is simple and efficient, with a time complexity of O(n), where n is the total number of strings in the input lists.