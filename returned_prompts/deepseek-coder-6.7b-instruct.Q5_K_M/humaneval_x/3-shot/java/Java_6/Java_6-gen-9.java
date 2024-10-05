        List<Integer> result = new ArrayList<>();
        for (String group : paren_string.split("\\s+")) {
            int current_depth = 0;
            int max_depth = 0;
            for (char c : group.toCharArray()) {
                if (c == '(') {
                    current_depth++;
                    if (current_depth > max_depth) {
                        max_depth = current_depth;
                    }
                } else if (c == ')') {
                    current_depth--;
                }
            }
            result.add(max_depth);
        }
        return result;
    }
}

