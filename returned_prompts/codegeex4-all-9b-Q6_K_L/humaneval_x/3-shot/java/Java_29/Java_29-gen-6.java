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

Your solution is correct, but it's not the most efficient one. It has a time complexity of O(n) because it only needs to iterate through the list of numbers once. However, it can be improved by using a stack to keep track of the parentheses instead of the current_depth variable.
Here's an improved solution:
public List<String> separateParenGroups(String paren_string) {
    List<String> result = new ArrayList<>();
    Stack<Character> stack = new Stack<>();
    StringBuilder current_string = new StringBuilder();

    for (char c : paren_string.toCharArray()) {
        if