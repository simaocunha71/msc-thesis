        List<Integer> result = new ArrayList<>();
        String[] groups = paren_string.split(" ");
        for (String group : groups) {
            int max_depth = 0;
            int level = 0;
            for (char c : group.toCharArray()) {
                if (c == '(') {
                    level++;
                } else {
                    level--;
                }
                if (level > max_depth) {
                    max_depth = level;
                }
            }
            result.add(max_depth);
        }
        return result;
    }
}
