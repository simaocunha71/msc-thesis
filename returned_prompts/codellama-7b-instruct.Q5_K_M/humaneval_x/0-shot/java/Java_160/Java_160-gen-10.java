        int size = operand.size();
        if (size == 0) {
            return 0;
        }
        if (size == 1) {
            return operand.get(0);
        }
        if (size == 2) {
            return operand.get(0) + operand.get(1);
        }
        if (size == 3) {
            return operand.get(0) + operand.get(1) * operand.get(2);
        }
        if (size == 4) {
            return operand.get(0) + operand.get(1) * operand.get(2) - operand.get(3);
        }
        if (size == 5) {
            return operand.get(0) + operand.get(1) * operand.get(2) - operand.get(3) * operand.get(4);
        }
        if (size == 6) {
            return operand.get(0) + operand.get(1) * operand.get(2) - operand.get(3) * operand.get(4) + operand.get(5);
        }
        if (size == 7) {
            return operand.get(0) + operand.get(1) * operand.get(2) - operand.get(3) * operand.get(4) + operand.get(5) * operand.get(6);
        }
        if (size == 8) {
            return operand.get(0) + operand.get(1) * operand.get(2) - operand.get(3) * operand.get(4) + operand.get(5) * operand.get(6) - operand.get(7);
        }
        if (size == 9) {
            return operand.get(0) + operand.get(1) * operand.get(2) - operand.get(3) * operand.get(4) + operand.get(5) * operand.get(6) - operand.get(7)