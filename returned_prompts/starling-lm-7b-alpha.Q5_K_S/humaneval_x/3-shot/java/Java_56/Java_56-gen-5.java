        Stack<Character> stack = new Stack<>();

        for (char c : brackets.toCharArray()) {
            if (c == '<') {
                stack.push(c);
            } else if (c == '>') {
                if (stack.size() == 0) return false;
                stack.pop();
            } else {
                return false;
            }
        }
        return stack.size() == 0;
    }
}


public class Main {
    public static void main(String[] args) {
        Solution solution = new Solution();
        System.out.println(solution.hasCloseElements(Arrays.asList(1.0, 2.0, 3.0), 0.5));
        System.out.println(solution.hasCloseElements(Arrays.asList(1.0, 2.8, 3.0, 4.0, 5.0, 2.0), 0.3));
        System.out.println(solution.separateParenGroups("( ) (( )) (( )( ))"));
        System.out.println(solution.separateParenGroups("( ( )( )( ))"));
        System.out.println(solution.truncateNumber(3.5));
        System.out.println(solution.correctBracketing("<"));
        System.out.println(solution.correctBracketing("<>"));
        System.out.println(solution.correctBracketing("<<><>>"));
        System.out.println(solution.correctBracketing("><<>"));
    }
}
```