        int len = operand.size();
        int[] a = new int[len];
        for (int i = 0; i < len; i++) {
            a[i] = operand.get(i);
        }
        int result = 0;
        for (int i = 0; i < len - 1; i++) {
            if (operator.get(i).equals("+")) {
                result += a[i] + a[i + 1];
            } else if (operator.get(i).equals("-")) {
                result -= a[i] - a[i + 1];
            } else if (operator.get(i).equals("*")) {
                result *= a[i] * a[i + 1];
            } else if (operator.get(i).equals("/")) {
                result /= a[i] / a[i + 1];
            } else if (operator.get(i).equals("**")) {
                result **= a[i] ** a[i + 1];
            }
        }
        return result;
    }
}

