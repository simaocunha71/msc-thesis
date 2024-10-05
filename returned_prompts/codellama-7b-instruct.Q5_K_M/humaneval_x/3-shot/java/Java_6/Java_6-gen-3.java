        List<Integer> result = new ArrayList<>();
        String[] groups = paren_string.split(" ");

        for (String group : groups) {
            int max_depth = 0;
            int current_depth = 0;
            for (char c : group.toCharArray()) {
                if (c == '(') {
                    current_depth += 1;
                } else if (c == ')') {
                    current_depth -= 1;
                    max_depth = Math.max(max_depth, current_depth);
                }
            }
            result.add(max_depth);
        }
        return result;
    }
}

