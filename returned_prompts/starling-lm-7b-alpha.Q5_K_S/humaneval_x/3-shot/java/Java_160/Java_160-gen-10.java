        Stack<Integer> operands = new Stack<>();
        Stack<Character> operators = new Stack<>();

        for (int i = 0; i < operator.size(); i++) {
            char current_operator = operator.get(i).charAt(0);
            int current_operand = operand.get(i);

            if (current_operator == '+' || current_operator == '-' || current_operator == '*' ||
                current_operator == '/' || current_operator == '^') {
                while (!operators.isEmpty()) {
                    char current_op = operators.peek();
                    if (current_op == '+' || current_op == '-') {
                        if (current_operator == '+' && current_op == '+') {
                            operands.push(current_operand);
                            break;
                        } else if (current_operator == '-' && current_op == '+') {
                            operands.push(current_operand);
                            break;
                        } else {
                            operands.push(operands.pop() * current_operand);
                            operators.pop();
                        }
                    } else if (current_op == '*' || current_op == '/') {
                        if (current_operator == '*' && current_op == '*') {
                            operands.push(current_operand);
                            break;
                        } else if (current_operator == '/' && current_op == '*') {
                            operands.push(current_operand);
                            break;
                        } else {
                            operands.push(operands.pop() * current_operand);
                            operators.pop();
                        }
                    } else if (current_op == '/') {
                        if (current_operator == '/' && current_op == '/') {
                            operands.push(current_operand);
                            break;
                        } else {
                            operands.push(operands.pop() / current_operand);
                            operators.pop();
                        }
                    } else if (current_op == '