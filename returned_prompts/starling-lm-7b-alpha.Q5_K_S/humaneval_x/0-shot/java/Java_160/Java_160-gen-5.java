        Stack<Integer> nums = new Stack<Integer>();
        Stack<Character> ops = new Stack<Character>();
        for (int i = 0; i < operand.size(); i++) {
            nums.push(operand.get(i));
        }

        for (int i = 0; i < operator.size(); i++) {
            char c = operator.get(i).charAt(0);
            if (c == '+' || c == '-') {
                if (ops.isEmpty()) {
                    ops.push(c);
                } else {
                    while (!ops.isEmpty() && (ops.peek() == '+' || ops.peek() == '-')) {
                        if (ops.peek() == '+') {
                            nums.push(nums.pop() + nums.pop());
                        } else {
                            nums.push(nums.pop() - nums.pop());
                        }
                        ops.pop();
                    }
                    ops.push(c);
                }
            } else if (c == '*' || c == '/') {
                if (ops.isEmpty()) {
                    ops.push(c);
                } else {
                    while (!ops.isEmpty() && (ops.peek() == '*' || ops.peek() == '/')) {
                        if (ops.peek() == '*') {
                            nums.push(nums.pop() * nums.pop());
                        } else {
                            nums.push(nums.pop() / nums.pop());
                        }
                        ops.pop();
                    }
                    ops.push(c);
                }
            } else if (c == '**') {
                if (ops.isEmpty()) {
                    ops.push(c);
                } else if (ops.peek() == '*') {
                    ops.push(c);
                } else {
                    while (!ops.isEmpty() && ops.peek() == '*') {
                        nums.push(nums.pop() * nums.