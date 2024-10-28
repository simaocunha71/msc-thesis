        int result = 0;
        for (int i = 0; i < operand.size(); i++) {
            if (i == 0) {
                result = operand.get(i);
            } else {
                int op = operator.get(i - 1).charAt(0);
                switch (op) {
                    case '+':
                        result += operand.get(i);
                        break;
                    case '-':
                        result -= operand.get(i);
                        break;
                    case '*':
                        result *= operand.get(i);
                        break;
                    case '/':
                        result /= operand.get(i);
                        break;
                    case '^':
                        result ^= operand.get(i);
                        break;
                }
            }
        }
        return result;
    }
}

