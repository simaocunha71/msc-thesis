        List<Integer> result = new ArrayList<>();
        int current_depth = 0;
        for (char c : paren_string.toCharArray()) {
            if (c == '(') {
                current_depth += 1;
            } else if (c == ')') {
                current_depth -= 1;
            }
            result.add(current_depth);
        }
        return result;
    }
}

