        int i = 0;
        int j = 0;
        int count = 1;
        int result = 0;
        while (j < operand.size()) {
            count++;
            switch (operator.get(i)) {
                case "+":
                    result += operand.get(j);
                    break;
                case "-":
                    result -= operand.get(j);
                    break;
                case "*":
                    result *= operand.get(j);
                    break;
                case "/":
                    result /= operand.get(j);
                    break;
                case "**":
                    result **= operand.get(j);
                    break;
            }
            j++;
            i++;
        }
        return result;
    }
}
