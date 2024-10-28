        List<Integer> result = new ArrayList<>();
        Stack<Integer> current_level = new Stack<>();

        for (String paren_group : paren_string.split(" ")) {
            int max_level = 0;
            for (char c : paren_group.toCharArray()) {
                if (c == '(') {
                    current_level.push(current_level.size() == 0 ? 1 : current_level.pop() + 1);
                } else if (c == ')') {
                    current_level.pop();
                }
                max_level = Math.max(max_level, current_level.size());
            }
            result.add(max_level);
        }
        return result;
    }
}

