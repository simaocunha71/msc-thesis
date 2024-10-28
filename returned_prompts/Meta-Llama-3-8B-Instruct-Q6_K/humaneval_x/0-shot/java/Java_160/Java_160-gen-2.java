    public int doAlgebra(List<String> operator, List<Integer> operand) {
        int result = operand.get(0);
        for (int i = 0; i < operator.size(); i++) {
            String op = operator.get(i);
            int num = operand.get(i + 1);
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
                    result = (int) Math.pow(result, num);
                    break;
                default:
                    throw new RuntimeException("Invalid operator");
            }
        }
        return result;
    }