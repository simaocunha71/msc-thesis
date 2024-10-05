        List<Integer> result = new ArrayList<>();
        String[] groups = paren_string.split(" ");
        for (String group : groups) {
            int maxDepth = 0;
            int currentDepth = 0;
            for (char c : group.toCharArray()) {
                if (c == '(') {
                    currentDepth++;
                    if (currentDepth > maxDepth) {
                        maxDepth = currentDepth;
                    }
                } else if (c == ')') {
                    currentDepth--;
                }
            }
            result.add(maxDepth);
        }
        return result;
    }
}

