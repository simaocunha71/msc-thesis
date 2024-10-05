Here is the Java implementation of the problem:

```java
import java.util.*;
import java.lang.*;

class Solution {
    public List<String> separateParenGroups(String paren_string) {
        paren_string = paren_string.replaceAll("\\s", ""); // remove all spaces
        List<String> paren_groups = new ArrayList<>();
        int start = 0;
        int depth = 0;
        for (int i = 0; i < paren_string.length(); i++) {
            if (paren_string.charAt(i) == '(') {
                if (depth == 0) {
                    start = i;
                }
                depth++;
            } else if (paren_string.charAt(i) == ')') {
                depth--;
                if (depth == 0) {
                    paren_groups.add(paren_string.substring(start, i + 1));
                }
            }
        }
        return paren_groups;
    }
}
```

This implementation works by iterating over the input string and keeping track of the depth of the parentheses. Each time the depth goes from 0 to 1, it means we've found the start of a new group. Each time the depth goes from 1 to 0, it means we've found the end of a group, and we can add it to the list of groups. The start and end indices of each group are also kept track of.

The time complexity of this solution is O(n), where n is the length of the input string. The space complexity is also O(n), since in the worst case we might have to store all the groups in the list.