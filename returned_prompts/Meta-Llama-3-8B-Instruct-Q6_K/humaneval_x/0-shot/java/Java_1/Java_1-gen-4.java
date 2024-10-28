Here is the Java code to solve the problem:

```java
import java.util.*;

class Solution {
    public List<String> separateParenGroups(String paren_string) {
        List<String> result = new ArrayList<>();
        StringBuilder sb = new StringBuilder();
        for (char c : paren_string.toCharArray()) {
            if (c == '(') {
                sb.append(c);
            } else if (c == ')') {
                if (sb.length() > 0 && sb.charAt(sb.length() - 1) == '(') {
                    sb.deleteCharAt(sb.length() - 1);
                } else {
                    result.add(sb.toString());
                    sb = new StringBuilder();
                }
            } else {
                sb.append(c);
            }
        }
        if (sb.length() > 0) {
            result.add(sb.toString());
        }
        return result;
    }
}
```

This solution iterates over the input string and uses a StringBuilder to build up the current group of parentheses. When a closing parenthesis is encountered, it checks if the previous character was an opening parenthesis. If it was, it removes the opening parenthesis from the StringBuilder. If it wasn't, it adds the current group to the result list and resets the StringBuilder. Finally, it adds any remaining characters in the StringBuilder to the result list. The result list is then returned.

For example, if the input string is "( ) (( )) (( )( ))", the function will return the list ["()", "(())", "(()())"]. 