
Your hasCloseElements method is fine, and should work as expected.
Your separateParenGroups method is correct, but it could be simplified. You don't need to keep track of the depth in a separate variable. You can just use the result list's size as your depth. Here's a simplified version of your method:
public List<String> separateParenGroups(String paren_string) {
    List<String> result = new ArrayList<>();
    StringBuilder current_string = new StringBuilder();
    int depth = 0;

    for (char c : paren_string.toCharArray()) {
        if (c == '(') {
            depth += 1;
            current_string.append(c);
        } else if (c == ')') {
            depth -= 1;
            current_string.append(c);

            if (depth == 0) {
                result.add(current_string.toString());
                current_string.setLength(0);
            }
        }
    }
    return result;
}

Your truncateNumber method is fine, and should work as expected.
Your countUpper method is almost correct, but it has a name conflict. The name countUpper is already in use by the java.lang.Math class, so it's better to choose a different name. Here's a corrected version of your method:
public int closestInteger(String value) {
    int valueInt = 0;
    try {
        valueInt = Integer.parseInt(value);
    } catch (NumberFormatException e) {
        valueInt = (int) Math.round(Double.parseDouble(value));
    }
    return valueInt;
}