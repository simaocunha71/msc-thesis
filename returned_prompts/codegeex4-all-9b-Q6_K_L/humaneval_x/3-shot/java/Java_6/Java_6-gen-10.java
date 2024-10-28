        List<Integer> result = new ArrayList<>();
        int max_depth = 0;
        int current_depth = 0;

        for (char c : paren_string.toCharArray()) {
            if (c == '(') {
                current_depth += 1;
                max_depth = Math.max(max_depth, current_depth);
            } else if (c == ')') {
                current_depth -= 1;
            }
            if (c == ' ' || c == ')') {
                result.add(max_depth);
                max_depth = 0;
                current_depth = 0;
            }
        }
        return result;
    }
}

