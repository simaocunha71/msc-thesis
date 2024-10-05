Here is the solution to the problem:

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

1.  We initialize two variables `total1` and `total2` to keep track of the total number of characters in each list.
2.  We iterate through each string in `lst1` and add its length to `total1`. We do the same for `lst2` and add its length to `total2`.
3.  We compare the values of `total1` and `total2`. If `total1` is less than `total2`, we return `lst1`. If `total1` is greater than `total2`, we return `lst2`.
4.  If `total1` is equal to `total2`, we return `lst1` because the problem statement specifies to return the first list if the two lists have the same number of chars.

This solution has a time complexity of O(n), where n is the total number of strings in both lists, because we iterate through each string once. The space complexity is O(1), which means the space required does not change with the size of the input lists, because we only use a constant amount of space to store the variables.