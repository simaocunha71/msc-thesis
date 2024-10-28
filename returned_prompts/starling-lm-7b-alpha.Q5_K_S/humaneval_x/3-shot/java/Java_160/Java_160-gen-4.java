        Stack<Integer> numbers = new Stack<>();
        for (int i = 0; i < operand.size(); i++) {
            numbers.push(operand.get(i));
        }

        while (operator.size() > 0) {
            String op = operator.remove(0);
            int b = numbers.pop();
            int a = numbers.pop();

            switch (op) {
                case "+":
                    numbers.push(a + b);
                    break;
                case "-":
                    numbers.push(a - b);
                    break;
                case "*":
                    numbers.push(a * b);
                    break;
                case "/":
                    numbers.push(a / b);
                    break;
                case "**":
                    numbers.push(a ** b);
                    break;
                default:
                    System.err.println("Invalid operator");
                    break;
            }
        }
        return numbers.pop();
    }
}


class Main {
    public static void main(String[] args) {
        Solution solution = new Solution();
        System.out.println(solution.hasCloseElements(Arrays.asList(1.0, 2.0, 3.0), 0.5));
        System.out.println(solution.hasCloseElements(Arrays.asList(1.0, 2.8, 3.0, 4.0, 5.0, 2.0), 0.3));
        System.out.println(solution.separateParenGroups("( ) (( )) (( )( ))"));
        System.out.println(solution.truncateNumber(3.5));
        System.out.println(solution.doAlgebra(
            Arrays.asList("+", "*", "-"),
            Arrays.asList(2, 3, 4, 5)
        ));
    }
}

```