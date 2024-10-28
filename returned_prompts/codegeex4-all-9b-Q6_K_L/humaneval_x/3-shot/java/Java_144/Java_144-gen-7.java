        List<String> result = new ArrayList<>();
        StringBuilder current_string = new StringBuilder();
        int current_depth = 0;

        for (char c : paren_string.toCharArray()) {
            if (c == '(') {
                current_depth += 1;
                current_string.append(c);
            } else if (c == ')') {
                current_depth -= 1;
                current_string.append(c);

                if (current_depth == 0) {
                    result.add(current_string.toString());
                    current_string.setLength(0);
                }
            }
        }
        return result;

    }

This method is correct and efficient. It has a time complexity of O(n) where n is the length of the input string.
The only thing I would suggest is to use a StringBuilder instead of a String to build the current_string. This is because strings