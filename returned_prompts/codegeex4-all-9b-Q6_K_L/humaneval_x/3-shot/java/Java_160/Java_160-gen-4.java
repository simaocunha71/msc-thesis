        int result = operand.get(0);

        for (int i = 1; i < operand.size(); i++) {
            String op = operator.get(i - 1);
            int current = operand.get(i);

            switch (op) {
                case "+":
                    result += current;
                    break;
                case "-":
                    result -= current;
                    break;
                case "*":
                    result *= current;
                    break;
                case "/":
                    result /= current;
                    break;
                case "**":
                    result = (int) Math.pow(result, current);
                    break;
            }
        }

        return result;
    }
}

