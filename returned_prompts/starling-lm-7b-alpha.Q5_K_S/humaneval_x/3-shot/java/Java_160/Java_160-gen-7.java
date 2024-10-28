        Stack<Integer> stack = new Stack<>();
        stack.push(operand.get(0));
        for (int i = 0; i < operator.size(); i++) {
            if (operator.get(i).equals("+")) {
                stack.push(operand.get(i + 1));
            } else if (operator.get(i).equals("-")) {
                stack.push(operand.get(i + 1));
            } else if (operator.get(i).equals("*")) {
                stack.push(operand.get(i + 1));
            } else if (operator.get(i).equals("/")) {
                stack.push(operand.get(i + 1));
            } else if (operator.get(i).equals("**")) {
                int a = stack.pop();
                int b = operand.get(i + 1);
                stack.push((int) Math.pow(a, b));
            }
        }
        return stack.pop();
    }
}

public class Main {
    public static void main(String[] args) {
        Solution solution = new Solution();
        System.out.println(solution.hasCloseElements(Arrays.asList(1.0, 2.0, 3.0), 0.5));
        System.out.println(solution.hasCloseElements(Arrays.asList(1.0, 2.8, 3.0, 4.0, 5.0, 2.0), 0.3));
        System.out.println(solution.separateParenGroups("( ) (( )) (( )( ))"));
        System.out.println(solution.truncateNumber(3.5));
        System.out.println(solution.doAlgebra(Arrays.asList("+", "*", "-"), Arrays.asList(2, 3, 4, 5)));
    }
}
```