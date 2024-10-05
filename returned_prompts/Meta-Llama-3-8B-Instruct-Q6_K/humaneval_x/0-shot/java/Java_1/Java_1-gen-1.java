    import java.util.*;

    class Solution {
        public List<String> separateParenGroups(String paren_string) {
            List<String> result = new ArrayList<>();
            StringBuilder sb = new StringBuilder();
            for (char c : paren_string.toCharArray()) {
                if (c == '(') {
                    sb.append('(');
                } else if (c == ')') {
                    result.add(sb.toString());
                    sb = new StringBuilder();
                }
            }
            result.add(sb.toString());
            return result;
        }
    }

Explanation:

1. We create an empty ArrayList `result` to store the separated groups.
2. We create a `StringBuilder` `sb` to build the current group.
3. We iterate over each character `c` in the input string `paren_string`.
4. If `c` is an open parenthesis `(`, we append it to `sb`.
5. If `c` is a close parenthesis `)`, we add the current group `sb.toString()` to `result` and reset `sb` to an empty string.
6. After the loop, we add the last group `sb.toString()` to `result`.
7. We return the `result` list.

This solution works by iterating over the input string and building each group as we go. When we encounter a close parenthesis, we add the current group to the result list and reset the group builder. This way, we separate the groups and add them to the result list. The last group is added after the loop, and the function returns the result list.