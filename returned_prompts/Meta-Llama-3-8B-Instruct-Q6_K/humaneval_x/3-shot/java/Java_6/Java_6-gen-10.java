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
        }

        for (String group : paren_string.split("\\s+")) {
            int depth = 0;
            for (char c : group.toCharArray()) {
                if (c == '(') {
                    depth += 1;
                } else if (c == ')') {
                    depth -= 1;
                }
            }
            result.add(Math.max(depth, 0));
        }
        return result;
    }
}

