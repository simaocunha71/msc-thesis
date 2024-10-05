Here is a Java solution using a stack data structure to keep track of the depth of nesting:

```java
import java.util.*;

class Solution {
    public List<Integer> parseNestedParens(String paren_string) {
        String[] groups = paren_string.split(" ");
        List<Integer> result = new ArrayList<>();
        for (String group : groups) {
            int depth = 0;
            int maxDepth = 0;
            for (char c : group.toCharArray()) {
                if (c == '(') {
                    depth++;
                    maxDepth = Math.max(depth, maxDepth);
                } else if (c == ')') {
                    depth--;
                }
            }
            result.add(maxDepth);
        }
        return result;
    }

    public static void main(String[] args) {
        Solution solution = new Solution();
        System.out.println(solution.parseNestedParens("(()()) ((())) () ((())()())"));  // [2, 3, 1, 3]
    }
}
```

Explanation:
The function `parseNestedParens` takes a string `paren_string` as input which represents multiple groups of nested parentheses separated by spaces. The function first splits the string into individual groups using the `split` method. Then it iterates through each group and calculates the maximum depth of nesting by using a stack data structure. The depth is increased by 1 whenever an opening parenthesis '(' is encountered and decreased by 1 whenever a closing parenthesis ')' is encountered. The maximum depth is stored in the `maxDepth` variable and added to the result list. Finally, the function returns the result list.