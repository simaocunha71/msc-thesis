        List<Integer> result = new ArrayList<Integer>();
        String[] groups = paren_string.split(" ");

        for (String group : groups) {
            int deepest_level = 0;
            Stack<Character> paren_stack = new Stack<Character>();

            for (char c : group.toCharArray()) {
                if (c == '(') {
                    paren_stack.push(c);
                }
                else if (c == ')') {
                    paren_stack.pop();
                }
            }

            while (!paren_stack.isEmpty()) {
                deepest_level += 1;
                paren_stack.pop();
            }

            result.add(deepest_level);
        }
        return result;
    }
}
