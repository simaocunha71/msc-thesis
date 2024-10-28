Here is the Java code that solves the problem:

```java
import java.util.*;
import java.lang.*;

class Solution {
    public String matchParens(List<String> lst) {
        int count = 0;
        for (String s : lst) {
            for (char c : s.toCharArray()) {
                if (c == '(') {
                    count++;
                } else if (c == ')') {
                    count--;
                }
                if (count < 0) {
                    return "No";
                }
            }
        }
        return count == 0 ? "Yes" : "No";
    }
}
```

This code iterates over the list of strings and over the characters of each string. It increments a counter when it encounters an open parenthesis and decrements it when it encounters a close parenthesis. If at any point the counter becomes negative, it means that the parentheses are not balanced and the function immediately returns "No". After iterating over all the strings, if the counter is zero, it means that all parentheses are balanced and the function returns "Yes". Otherwise, it returns "No".