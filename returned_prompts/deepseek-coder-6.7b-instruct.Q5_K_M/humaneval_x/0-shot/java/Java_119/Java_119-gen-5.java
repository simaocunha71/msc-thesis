    import java.util.*;
    import java.lang.*;

    class Solution {
        public String matchParens(List<String> lst) {
            String str1 = lst.get(0);
            String str2 = lst.get(1);

            if (isBalanced(str1) && isBalanced(str2)) {
                return "Yes";
            } else if (!isBalanced(str1) && !isBalanced(str2)) {
                return "No";
            } else {
                return "Yes";
            }
        }

        public boolean isBalanced(String str) {
            Stack<Character> stack = new Stack<>();
            for (int i = 0; i < str.length(); i++) {
                char c = str.charAt(i);
                if (c == '(') {
                    stack.push(c);
                } else if (c == ')' && !stack.isEmpty()) {
                    stack.pop();
                } else {
                    return false;
                }
            }
            return stack.isEmpty();
        }
    }

