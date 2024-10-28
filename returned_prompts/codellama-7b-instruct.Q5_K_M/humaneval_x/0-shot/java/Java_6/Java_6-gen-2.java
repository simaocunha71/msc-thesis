        List<Integer> result = new ArrayList<>();
        for (String paren_group: paren_string.split(" ")) {
            int level = 0;
            for (char c: paren_group.toCharArray()) {
                if (c == '(') {
                    level++;
                } else if (c == ')') {
                    level--;
                }
            }
            result.add(level);
        }
        return result;
    }
}