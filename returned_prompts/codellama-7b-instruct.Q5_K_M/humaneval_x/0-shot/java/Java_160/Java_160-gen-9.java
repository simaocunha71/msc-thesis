        int len = operand.size();
        if (len < 2)
            return -1;
        if (operator.size() != len - 1)
            return -1;

        int res = operand.get(0);
        for (int i = 1; i < len; i++) {
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
                default:
                    break;
            }
        }
        return res;
    }
}
