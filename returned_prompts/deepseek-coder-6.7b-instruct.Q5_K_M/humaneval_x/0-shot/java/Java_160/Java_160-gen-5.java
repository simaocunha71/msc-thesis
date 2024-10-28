        int res = operand.get(0);

        for (int i = 1; i < operand.size(); i++) {
            switch (operator.get(i - 1)) {
                case "+":
                    res += operand.get(i);
                    break;
                case "-":
                    res -= operand.get(i);
                    break;
                case "*":
                    res *= operand.get(i);
                    break;
                case "/":
                    res /= operand.get(i);
                    break;
                case "**":
                    res = (int) Math.pow(res, operand.get(i));
                    break;
            }
        }

        return res;
    }
}



