Here is a solution to the problem using Java:

```java
import java.util.*;
import java.lang.*;

class Solution {
    public String matchParens(List<String> lst) {
        int openCount = 0;
        int closeCount = 0;
        for (String str : lst) {
            for (char c : str.toCharArray()) {
                if (c == '(') {
                    openCount++;
                } else if (c == ')') {
                    closeCount++;
                }
                if (closeCount > openCount) {
                    return "No";
                }
            }
        }
        if (openCount == closeCount) {
            return "Yes";
        } else {
            return "No";
        }
    }
}
```

The above solution iterates over the list of strings and counts the number of open and close parentheses. If the number of close parentheses is ever greater than the number of open parentheses, it returns "No" because the parentheses are not balanced. If the number of open and close parentheses are equal, it returns "Yes" because the parentheses are balanced. Otherwise, it returns "No".