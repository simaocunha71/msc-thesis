        List<Integer> result = new ArrayList<>();
        int max_depth = 0;
        int current_depth = 0;
        StringBuilder current_string = new StringBuilder();

        for (char c : paren_string.toCharArray()) {
            if (c == '(') {
                current_depth += 1;
                current_string.append(c);
            } else if (c == ')') {
                current_depth -= 1;
                current_string.append(c);

                if (current_depth == 0) {
                    result.add(current_depth);
                    max_depth = Math.max(max_depth, current_depth);
                    current_string.setLength(0);
                }
            }
        }
        return result;
    }
}

