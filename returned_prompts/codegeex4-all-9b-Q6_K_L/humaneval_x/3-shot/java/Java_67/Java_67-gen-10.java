
The first question is already correctly solved, so we will move on to the second question.
The solution is almost correct, but the condition for adding the current_string to result is wrong. It should be when current_depth is 0, not when it is 1. This is because the current_depth is incremented when we encounter an open parenthesis and decremented when we encounter a closed parenthesis. So, when we encounter the first closed parenthesis, the current_depth will be 0, not 1. We need to add the current_string to result when the current_depth is 0, so that we don't miss any groups.
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
    return result;
}

The third question is already correctly solved, so we will move on to the fourth question.
The solution is almost correct, but the condition for parsing the number is wrong. It should be if (part.contains("apples") || part.contains("oranges")), not if (part.contains("apples") && part.contains("oranges")). This is because the string s can contain both "apples" and "oranges" in any order. We need to parse the number when we encounter either "apples" or "oranges", not when we encounter both.
Here is the corrected code:
public int fruitDistribution(String s, int n) {
    int apples = 0;
    int oranges = 0;

    for (String part : s.split(" ")) {
        try {
           