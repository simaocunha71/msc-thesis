        List<Integer> result = new ArrayList<>();
        List<String> group_strings = Arrays.asList(paren_string.split(" "));

        for (String group_string : group_strings) {
            int current_depth = 0;
            int max_depth = 0;

            for (char c : group_string.toCharArray()) {
                if (c == '(') {
                    current_depth += 1;
                } else if (c == ')') {
                    current_depth -= 1;

                    if (current_depth > max_depth) {
                        max_depth = current_depth;
                    }
                }
            }
            result.add(max_depth);
        }
        return result;
    }
}

