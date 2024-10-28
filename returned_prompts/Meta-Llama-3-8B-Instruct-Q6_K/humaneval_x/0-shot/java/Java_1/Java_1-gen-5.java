Here is a Java solution to separate the nested parentheses into separate strings:

```java
import java.util.*;

class Solution {
    public List<String> separateParenGroups(String paren_string) {
        List<String> result = new ArrayList<>();
        StringBuilder current = new StringBuilder();
        boolean inParen = false;

        for (char c : paren_string.toCharArray()) {
            if (c == '(') {
                inParen = true;
                current.append(c);
            } else if (c == ')') {
                if (inParen) {
                    current.append(c);
                    result.add(current.toString());
                    current = new StringBuilder();
                    inParen = false;
                }
            } else {
                if (inParen) {
                    current.append(c);
                }
            }
        }

        return result;
    }
}
```

In this solution, we iterate over the input string and build a current string as we go. When we encounter a '(', we start building the current string, and when we encounter a ')', we add the current string to the result list and reset the current string. If we are not inside a parentheses group, we simply add the current character to the current string. At the end of the input string, we add the last current string to the result list if it's not empty. The result is a list of strings, each representing a group of balanced parentheses.