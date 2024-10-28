        List<Integer> result = new ArrayList<>();
        String[] groups = paren_string.split(" ");
        for (String group : groups) {
            int depth = 0;
            int max_depth = 0;
            for (char c : group.toCharArray()) {
                if (c == '(') {
                    depth += 1;
                    max_depth = Math.max(depth, max_depth);
                } else if (c == ')') {
                    depth -= 1;
                }
            }
            result.add(max_depth);
        }
        return result;

    }
}

