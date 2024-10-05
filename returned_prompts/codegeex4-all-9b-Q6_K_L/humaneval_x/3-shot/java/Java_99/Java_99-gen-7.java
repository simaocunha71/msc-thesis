
Your code for separateParenGroups is almost correct.  However, it will not work if there are parentheses in the middle of a group.  For example, separateParenGroups("(())())") will return ["()", "()()"] instead of ["()()", "()()"].  You can fix this by checking if the current depth is 0 after the loop, and if so, add the current_string to the result list.
Here is the corrected code:
public List<String> separateParenGroups(String paren_string) {
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

    if (current_depth == 0) {
        result.add(current_string.toString());
    }

    return result;
}

Your code for truncateNumber is correct.

Your code for countUpper is correct.