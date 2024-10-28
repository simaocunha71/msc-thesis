Here is the solution in Java:

```java
import java.util.*;

class Solution {
    public List<String> totalMatch(List<String> lst1, List<String> lst2) {
        int total1 = 0, total2 = 0;
        for (String s : lst1) {
            total1 += s.length();
        }
        for (String s : lst2) {
            total2 += s.length();
        }
        if (total1 < total2) {
            return lst1;
        } else if (total1 > total2) {
            return lst2;
        } else {
            return lst1;
        }
    }
}
```

This solution works by first calculating the total number of characters in each list. It then compares these totals and returns the list with the smaller total. If the two totals are equal, it returns the first list. This solution has a time complexity of O(n), where n is the total number of strings in both lists, since it needs to iterate over each string in both lists once. It has a space complexity of O(1), since it only uses a constant amount of space to store the totals.