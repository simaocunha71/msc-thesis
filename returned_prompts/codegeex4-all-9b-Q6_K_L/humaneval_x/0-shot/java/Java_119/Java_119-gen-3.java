Here is a Java solution for the problem:

```java
import java.util.*;
import java.lang.*;

class Solution {
    public String matchParens(List<String> lst) {
        int open = 0, close = 0;
        for (String s : lst) {
            for (char c : s.toCharArray()) {
                if (c == '(') open++;
                else close++;
            }
        }
        return (open == close) ? "Yes" : "No";
    }
}
```

This program works by iterating over each character in the concatenated string. For each open parenthesis it sees, it increments the `open` counter and for each close parenthesis, it increments the `close` counter. If the number of open and close parentheses are equal, then the string is good and we return "Yes". Otherwise, we return "No".