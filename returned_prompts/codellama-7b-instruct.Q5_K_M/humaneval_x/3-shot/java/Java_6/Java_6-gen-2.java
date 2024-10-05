        List<Integer> result = new ArrayList<>();
        int current_depth = 0;
        int max_depth = 0;

        for (char c : paren_string.toCharArray()) {
            if (c == '(') {
                current_depth += 1;
            } else if (c == ')') {
                current_depth -= 1;
                max_depth = Math.max(max_depth, current_depth);
            }
        }
        for (int i = 0; i < paren_string.length(); i++) {
            if (paren_string.charAt(i) == ' ') {
                result.add(max_depth);
                max_depth = 0;
            }
        }
        result.add(max_depth);
        return result;
    }
}

