Here is the Java code to solve the problem:

```java
import java.util.*;

class Solution {
    public List<Integer> parseNestedParens(String paren_string) {
        List<Integer> levels = new ArrayList<>();
        StringBuilder sb = new StringBuilder();
        for (char c : paren_string.toCharArray()) {
            if (c == '(') {
                sb.append(c);
            } else if (c == ')') {
                levels.add(sb.length());
                sb.deleteCharAt(sb.length() - 1);
            }
        }
        return levels;
    }
}
```
In this code, we iterate over each character in the input string. If the character is an open parenthesis, we append it to a StringBuilder. If the character is a close parenthesis, we add the length of the StringBuilder (which represents the current level of nesting) to our list of levels and then remove the last character from the StringBuilder (which represents the previous level of nesting). At the end of the function, we return the list of levels.

The time complexity of this function is O(n), where n is the length of the input string, because we make one pass over the input string. The space complexity is O(n) as well, because in the worst case, we might need to store all characters in the StringBuilder.