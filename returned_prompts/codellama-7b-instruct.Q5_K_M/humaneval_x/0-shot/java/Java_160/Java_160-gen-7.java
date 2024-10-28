        int n = operator.size();
        int m = operand.size();
        int result = operand.get(0);
        for(int i = 0; i < n; i++) {
            String op = operator.get(i);
            if(op.equals("+")) {
                result += operand.get(i + 1);
            } else if(op.equals("-")) {
                result -= operand.get(i + 1);
            } else if(op.equals("*")) {
                result *= operand.get(i + 1);
            } else if(op.equals("/")) {
                result /= operand.get(i + 1);
            } else if(op.equals("**")) {
                result = result * operand.get(i + 1);
            }
        }
        return result;
    }
}
