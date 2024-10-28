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

This is a good solution, but it can be improved. You're using a StringBuilder to build the current string, which is good, but you're not using it to your advantage. You can use it to keep track of the current depth, and then you can use it to build the current string. Here's how you can do it:

public List<String> separateParenGroups(String paren_string