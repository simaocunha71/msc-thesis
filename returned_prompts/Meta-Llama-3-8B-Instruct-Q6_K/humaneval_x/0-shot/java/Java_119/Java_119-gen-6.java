Here is a Java solution:

```java
import java.util.*;

class Solution {
    public String matchParens(List<String> lst) {
        int open = 0, close = 0;
        for (String s : lst) {
            for (char c : s.toCharArray()) {
                if (c == '(') open++;
                else close++;
            }
        }
        if ((open + close) % 2 != 0) return "No";
        if (open != close) return "No";
        return "Yes";
    }
}
```

This solution iterates through the list of strings and counts the number of open and close parentheses. If the total number of parentheses is odd, it's impossible to make a good string, so the function returns "No". If the number of open and close parentheses are not equal, it's also impossible to make a good string, so the function returns "No". If both conditions are met, the function returns "Yes".