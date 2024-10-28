        List<Integer> result = new ArrayList<>();
        StringBuilder current_string = new StringBuilder();
        int current_depth = 0;
        int max_depth = 0;

        for (char c : paren_string.toCharArray()) {
            if (c == '(') {
                current_depth += 1;
                current_string.append(c);
                if (current_depth > max_depth) {
                    max_depth = current_depth;
                }
            } else if (c == ')') {
                current_depth -= 1;
                current_string.append(c);
            }
        }
        result.add(max_depth);
        return result;

    }
}

