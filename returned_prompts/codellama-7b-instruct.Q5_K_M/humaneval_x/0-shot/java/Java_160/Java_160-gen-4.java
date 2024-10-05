        int result = 0;
        for (int i = 0; i < operator.size(); i++) {
            String op = operator.get(i);
            int val = operand.get(i);
            switch (op) {
                case "+":
                    result += val;
                    break;
                case "-":
                    result -= val;
                    break;
                case "*":
                    result *= val;
                    break;
                case "/":
                    result /= val;
                    break;
                case "^":
                    result ^= val;
                    break;
                default:
                    break;
            }
        }
        return result;
    }

    public int doAlgebra2(List<String> operator, List<Integer> operand) {
        int result = 0;
        for (int i = 0; i < operator.size(); i++) {
            String op = operator.get(i);
            int val = operand.get(i);
            switch (op) {
                case "+":
                    result = result + val;
                    break;
                case "-":
                    result = result - val;
                    break;
                case "*":
                    result = result * val;
                    break;
                case "/":
                    result = result / val;
                    break;
                case "^":
                    result = result ^ val;
                    break;
                default:
                    break;
            }
        }
        return result;
    }
}




