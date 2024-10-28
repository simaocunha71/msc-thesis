The task is to write a program in Java that takes a string of parentheses as input and returns a list of integers, where each integer represents the maximum level of nesting for each group of parentheses in the input string.

Here is the solution to this problem:

```java
import java.util.*;

class Solution {
    public List<Integer> parseNestedParens(String paren_string) {
        List<Integer> result = new ArrayList<>();
        StringBuilder sb = new StringBuilder();
        for (char c : paren_string.toCharArray()) {
            if (c == '(') {
                sb.append(c);
            } else if (c == ')') {
                if (sb.length() > 0) {
                    sb.deleteCharAt(sb.length() - 1);
                } else {
                    result.add(sb.length());
                    sb.delete(0, sb.length());
                }
            }
        }
        result.add(sb.length());
        return result;
    }
}
```

This solution iterates over the input string, and whenever it encounters a '(', it appends it to a StringBuilder. Whenever it encounters a ')', it checks if the StringBuilder is not empty. If it's not empty, it removes the last character (which is '('). If the StringBuilder is empty, it means that the ')' is closing a group of parentheses, so it adds the length of the StringBuilder to the result list and resets the StringBuilder. Finally, after iterating over the entire string, it adds the length of the remaining characters in the StringBuilder to the result list. This gives the maximum level of nesting for each group of parentheses. The result list is returned as the output.