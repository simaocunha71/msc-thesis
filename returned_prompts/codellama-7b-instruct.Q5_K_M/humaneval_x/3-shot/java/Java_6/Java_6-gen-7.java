        List<Integer> result = new ArrayList<>();
        String[] groups = paren_string.split(" ");
        for (String group : groups) {
            int depth = 0;
            for (char c : group.toCharArray()) {
                if (c == '(') {
                    depth += 1;
                } else if (c == ')') {
                    depth -= 1;
                }
            }
            result.add(depth);
        }
        return result;
    }
}

