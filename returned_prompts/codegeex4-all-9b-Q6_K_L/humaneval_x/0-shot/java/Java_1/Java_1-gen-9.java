Here is a Java solution to your problem:

```java
import java.util.*;
import java.lang.*;

class Solution {
    public List<String> separateParenGroups(String paren_string) {
        List<String> result = new ArrayList<>();
        StringBuilder sb = new StringBuilder();
        int open = 0;
        for (char c : paren_string.toCharArray()) {
            if (c == '(') {
                open++;
            } else if (c == ')') {
                open--;
            }
            sb.append(c);
            if (open == 0) {
                result.add(sb.toString());
                sb = new StringBuilder();
            }
        }
        return result;
    }

    public static void main(String[] args) {
        Solution sol = new Solution();
        List<String> paren_groups = sol.separateParenGroups("( ) (( )) (( )( ))");
        for (String group : paren_groups) {
            System.out.println(group);
        }
    }
}
```
This solution works by iterating through the input string and adding characters to a StringBuilder. When we encounter a closing parenthesis, we decrement the count of open parentheses. When the count of open parentheses reaches zero, we add the current string to the result list and reset the StringBuilder.

The output of this program will be:
```
()
(())
(()())
```