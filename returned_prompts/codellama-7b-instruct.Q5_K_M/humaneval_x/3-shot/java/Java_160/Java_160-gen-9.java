        int result = operand.get(0);
        int current_index = 1;

        while (!operator.isEmpty()) {
            String current_operator = operator.remove(0);
            int current_operand = operand.remove(0);

            switch (current_operator) {
                case "+":
                    result += current_operand;
                    break;
                case "-":
                    result -= current_operand;
                    break;
                case "*":
                    result *= current_operand;
                    break;
                case "/":
                    result /= current_operand;
                    break;
                case "**":
                    result = (int) Math.pow(result, current_operand);
                    break;
            }
        }
        return result;
    }
}

