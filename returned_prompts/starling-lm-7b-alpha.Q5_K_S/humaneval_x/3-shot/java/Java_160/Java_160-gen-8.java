        Stack<Integer> numbers = new Stack<>();
        Stack<String> operations = new Stack<>();

        for (int i = 0; i < operator.size(); i++) {
            String current_operator = operator.get(i);
            Integer current_operand = operand.get(i);

            if (current_operator.equals("+")) {
                operations.push(current_operator);
                numbers.push(current_operand);
            } else if (current_operator.equals("-")) {
                operations.push(current_operator);
                numbers.push(current_operand);
            } else if (current_operator.equals("*")) {
                operations.push(current_operator);
                numbers.push(current_operand);
            } else if (current_operator.equals("/")) {
                operations.push(current_operator);
                numbers.push(current_operand);
            } else {
                int current_number = numbers.pop();
                int result = 1;
                while (operations.size() > 0) {
                    String current_operation = operations.pop();
                    if (current_operation.equals("+")) {
                        result += current_number;
                    } else if (current_operation.equals("-")) {
                        result -= current_number;
                    } else if (current_operation.equals("*")) {
                        result *= current_number;
                    } else if (current_operation.equals("/")) {
                        result /= current_number;
                    }
                }
                numbers.push(result);
            }
        }
        return numbers.pop();
    }
}


```