        int left = operand.get(0);
        int right = operand.get(1);
        for (int i = 2; i < operand.size(); i++) {
            String operation = operator.get(i - 1);
            int result = 0;
            switch (operation) {
                case "+":
                    result = left + right;
                    break;
                case "-":
                    result = left - right;
                    break;
                case "*":
                    result = left * right;
                    break;
                case "/":
                    result = left / right;
                    break;
                case "**":
                    result = (int) Math.pow(left, right);
                    break;
            }
            left = result;
            right = operand.get(i);
        }
        return result;
    }
}

