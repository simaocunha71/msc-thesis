        List<Integer> result = new ArrayList<>();
        Stack<Integer> paren_depth = new Stack<>();
        paren_depth.push(0);

        for (char c : paren_string.toCharArray()) {
            if (c == '(') {
                paren_depth.push(paren_depth.peek() + 1);
            } else if (c == ')') {
                paren_depth.pop();
            }
        }

        for (int depth : paren_depth) {
            result.add(depth);
        }
        return result;
    }
}

