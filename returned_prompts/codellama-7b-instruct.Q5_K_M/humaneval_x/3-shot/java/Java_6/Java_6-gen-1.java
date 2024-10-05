        List<Integer> result = new ArrayList<>();
        for (String group : paren_string.split(" ")) {
            int current_depth = 0;
            for (char c : group.toCharArray()) {
                if (c == '(') {
                    current_depth++;
                } else if (c == ')') {
                    current_depth--;
                }
            }
            result.add(current_depth);
        }
        return result;
    }
}

