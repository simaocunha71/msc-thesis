```java
import java.util.*;
import java.lang.*;

class Solution {
    public List<String> separateParenGroups(String paren_string) {
        List<String> result = new ArrayList<>();
        StringBuilder sb = new StringBuilder();
        int count = 0;

        for (int i = 0; i < paren_string.length(); i++) {
            char c = paren_string.charAt(i);

            if (c == ' ') {
                continue;
            }

            if (c == '(') {
                count++;
            } else if (c == ')') {
                count--;
            }

            sb.append(c);

            if (count == 0) {
                result.add(sb.toString());
                sb.setLength(0);
            }
        }

        return result;
    }

    public static void main(String[] args) {
        Solution solution = new Solution();
        System.out.println(solution.separateParenGroups("( ) (( )) (( )( ))"));
    }
}
```

Explanation:
The `separateParenGroups` function iterates through the input string `paren_string` and keeps track of the number of open parentheses using the `count` variable. If the current character is an open parenthesis, it increments `count`. If the current character is a close parenthesis, it decrements `count`. Whenever `count` reaches 0, it means that a group of balanced parentheses has been found, so the function adds the group to the `result` list and resets the `sb` StringBuilder to an empty string. Finally, it returns the `result` list.

In the `main` function, we create an instance of the `Solution` class and call the `separateParenGroups` function with the input string. The result is printed to the console.