        List<Integer> result = new ArrayList<>();
        int current_depth = 0;

        String[] paren_groups = paren_string.split(" ");
        for (String group : paren_groups) {
            int max_depth = 0;
            for (char c : group.toCharArray()) {
                if (c == '(') {
                    current_depth += 1;
                    max_depth = Math.max(max_depth, current_depth);
                } else if (c == ')') {
                    current_depth -= 1;
                }
            }
            result.add(max_depth);
        }
        return result;
    }
}

