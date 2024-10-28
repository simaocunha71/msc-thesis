        List<Integer> max_nesting_levels = new ArrayList<>();
        Stack<Integer> stack = new Stack<>();

        String[] groups = paren_string.split(" ");
        for (String group : groups) {
            int nesting_level = 0;
            for (int i = 0; i < group.length(); i++) {
                char c = group.charAt(i);
                if (c == '(') {
                    stack.push(nesting_level);
                } else if (c == ')') {
                   