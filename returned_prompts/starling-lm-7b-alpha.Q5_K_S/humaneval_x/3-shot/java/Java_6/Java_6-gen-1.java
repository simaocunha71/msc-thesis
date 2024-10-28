        List<Integer> result = new ArrayList<>();
        StringBuilder current_string = new StringBuilder();
        int current_depth = 0;

        for (char c : paren_string.toCharArray()) {
            if (c == '(') {
                current_depth += 1;
                current_string.append(c);
            } else if (c == ')') {
                current_depth -= 1;
                current_string.append(c);

                if (current_depth == Math.max(0, current_depth)) {
                    result.add(current_depth);
                    current_string.setLength(0);
                    current_depth = 0;
                }
            }
        }
        return result;
    }
}

