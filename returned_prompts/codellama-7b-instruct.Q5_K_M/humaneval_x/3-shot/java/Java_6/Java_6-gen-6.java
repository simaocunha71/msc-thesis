        List<Integer> result = new ArrayList<>();
        for (String paren_group : paren_string.trim().split(" ")) {
            int max_depth = 0;
            int current_depth = 0;
            for (char c : paren_group.toCharArray()) {
                if (c == '(') {
                    current_depth += 1;
                } else if (c == ')') {
                    current_depth -= 1;
                }

                if (current_depth > max_depth) {
                    max_depth = current_depth;
                }
            }
            result.add(max_depth);
        }
        return result;
    }
}

