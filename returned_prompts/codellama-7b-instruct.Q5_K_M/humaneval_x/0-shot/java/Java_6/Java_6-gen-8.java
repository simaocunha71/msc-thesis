        List<Integer> deepest_levels = new ArrayList<Integer>();

        for (String paren_group : paren_string.split(" ")) {
            int deepest_level = 0;
            int open_parens = 0;

            for (char paren : paren_group.toCharArray()) {
                if (paren == '(') {
                    open_parens++;
                    deepest_level = Math.max(deepest_level, open_parens);
                } else if (paren == ')') {
                    open_parens--;
                }
            }
            deepest_levels.add(deepest_level);
        }
        return deepest_levels;
    }
}
