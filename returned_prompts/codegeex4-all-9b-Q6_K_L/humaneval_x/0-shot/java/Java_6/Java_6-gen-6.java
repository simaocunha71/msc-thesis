```java
import java.util.*;
import java.lang.*;

class Solution {
    public List<Integer> parseNestedParens(String paren_string) {
        List<Integer> result = new ArrayList<>();
        String[] groups = paren_string.split(" ");
        for (String group : groups) {
            int depth = 0;
            int max_depth = 0;
            for (char c : group.toCharArray()) {
                if (c == '(') {
                    depth++;
                    max_depth = Math.max(depth, max_depth);
                } else if (c == ')') {
                    depth--;
                }
            }
            result.add(max_depth);
        }
        return result;
    }
}
```
The code first splits the input string into individual groups using the `split` method. Then, for each group, it initializes a depth counter and a maximum depth counter. It then iterates through each character in the group. If the character is an opening parenthesis `(`, it increases the depth counter and updates the maximum depth counter. If the character is a closing parenthesis `)`, it decreases the depth counter. Finally, it adds the maximum depth for the group to the result list. The method returns the result list.