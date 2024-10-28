Here is the Java code for the problem:

```java
import java.util.*;

class Solution {
    public List<String> totalMatch(List<String> lst1, List<String> lst2) {
        int total1 = 0, total2 = 0;
        for (String str : lst1) {
            total1 += str.length();
        }
        for (String str : lst2) {
            total2 += str.length();
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

Explanation:

The function `totalMatch` takes two lists of strings, `lst1` and `lst2`, as input. It calculates the total number of characters in each list by iterating over each string in the list and summing up the length of each string. 

Then it compares the two totals. If `total1` is less than `total2`, it returns `lst1`. If `total1` is greater than `total2`, it returns `lst2`. If the two totals are equal, it returns `lst1` because the problem statement says to return the first list in case of a tie. 

This solution has a time complexity of O(n), where n is the total number of strings in both lists, because it iterates over each string in both lists once. The space complexity is O(1), because it uses a constant amount of space to store the totals. 