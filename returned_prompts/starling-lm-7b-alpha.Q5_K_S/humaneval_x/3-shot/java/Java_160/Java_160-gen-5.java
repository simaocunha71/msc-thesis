        Stack<Integer> numbers = new Stack<>();
        for (int i = 0; i < operand.size(); i++) {
            numbers.push(operand.get(i));
        }

        Stack<Character> operations = new Stack<>();
        for (String op : operator) {
            operations.push(op.charAt(0));
        }

        while (!operations.isEmpty()) {
            char op = operations.pop();
            switch (op) {
                case '+':
                    numbers.push(numbers.pop() + numbers.pop());
                    break;
                case '-':
                    int temp = numbers.pop();
                    numbers.push(numbers.pop() - temp);
                    break;
                case '*':
                    numbers.push(numbers.pop() * numbers.pop());
                    break;
                case '/':
                    temp = numbers.pop();
                    numbers.push(numbers.pop() / temp);
                    break;
                case '**':
                    temp = numbers.pop();
                    numbers.push((int)Math.pow(numbers.pop(), temp));
                    break;
            }
        }
        return numbers.pop();
    }
}

