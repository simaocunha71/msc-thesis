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
        return (count == 0) ? "Yes" : "No";
    }

    public static void main(String[] args) {
        Solution sol = new Solution();
        System.out.println(sol.matchParens(Arrays.asList("()(", ")"))); // "Yes"
        System.out.println(sol.matchParens(Arrays.asList(")", ")"))); // "No"
    }
}
```

This code works by iterating over the characters in the strings in the list. For each open parenthesis '(', it increments a counter, and for each close parenthesis ')', it decrements the counter. If the counter ever goes negative, it means there are more close parentheses than open ones, so the string is not good. Finally, after checking all characters in all strings, if the counter is zero, it means all parentheses are balanced and the string is good. Otherwise, it's not.