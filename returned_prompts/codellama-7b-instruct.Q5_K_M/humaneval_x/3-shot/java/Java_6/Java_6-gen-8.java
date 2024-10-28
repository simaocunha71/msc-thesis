        List<Integer> result = new ArrayList<>();
        int max_depth = 0;
        int current_depth = 0;
        boolean is_open = false;

        for (char c : paren_string.toCharArray()) {
            if (c == '(') {
                current_depth += 1;
                is_open = true;
            } else if (c == ')') {
                current_depth -= 1;
                is_open = false;
            }

            if (current_depth > max_depth) max_depth = current_depth;
        }
        result.add(max_depth);
        return result;

    }
}

