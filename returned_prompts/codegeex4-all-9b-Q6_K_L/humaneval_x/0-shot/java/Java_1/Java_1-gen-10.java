Here is the Java code that separates the groups of nested parentheses:

```java
import java.util.*;
import java.lang.*;

class Solution {
    public List<String> separateParenGroups(String paren_string) {
        List<String> result = new ArrayList<>();
        StringBuilder currentGroup = new StringBuilder();
        int openCount = 0;

        for (char c : paren_string.toCharArray()) {
            if (c == '(') {
                openCount++;
                currentGroup.append(c);
            } else if (c == ')') {
                openCount--;
                currentGroup.append(c);
                if (openCount == 0) {
                    result.add(currentGroup.toString());
                    currentGroup.setLength(0);
                }
            }
        }

        return result;
    }

    public static void main(String[] args) {
        Solution solution = new Solution();
        System.out.println(solution.separateParenGroups("( ) (( )) (( )( ))"));  // ["()", "(())", "(()())"]
    }
}
```

Explanation:
This code iterates over each character in the input string. If it encounters an opening parenthesis '(', it increments the openCount and appends the character to the currentGroup. If it encounters a closing parenthesis ')', it decrements the openCount and appends the character to the currentGroup. If the openCount becomes 0, it means that a complete group of parentheses has been found and it is added to the result list.