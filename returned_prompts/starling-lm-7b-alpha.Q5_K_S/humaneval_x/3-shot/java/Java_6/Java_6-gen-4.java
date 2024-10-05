        List<Integer> result = new ArrayList<>();
        int depth = 0;

        for (char c : paren_string.toCharArray()) {
            if (c == '(') {
                depth += 1;
            } else if (c == ')') {
                depth -= 1;
            }
            result.add(depth);
        }
        return result;
    }
}

