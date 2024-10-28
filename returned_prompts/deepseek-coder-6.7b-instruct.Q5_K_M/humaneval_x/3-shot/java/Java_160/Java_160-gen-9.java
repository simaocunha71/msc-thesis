        int result = operand.get(0);
        for (int i = 1; i < operand.size(); i++) {
            String op = operator.get(i - 1);
            int num = operand.get(i);
            switch (op) {
                case "+":
                    result += num;
                    break;
                case "-":
                    result -= num;
                    break;
                case "*":
                    result *= num;
                    break;
                case "/":
                    result /= num;
                    break;
                case "**":
                    result = (int)Math.pow(result, num);
                    break;
            }
        }
        return result;
     }
}

