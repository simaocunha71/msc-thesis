
I think the first question is not well-worded. The question asks to check if there are any two numbers closer than the given threshold, but it doesn't say what to do if there are no numbers. The function should return false if there are no numbers. So I would change the question to:

Given a list of numbers, find two numbers in the list that are closer than the given threshold. If there are no numbers or if no two numbers are closer than the threshold, return -1.

And I would change the function to:
public double hasCloseElements(List<Double> numbers, double threshold) {
    if (numbers.size() < 2) {
        return -1;
    }
    for (int i = 0; i < numbers.size(); i++) {
        for (int j = i + 1; j < numbers.size(); j++) {
            double distance = Math.abs(numbers.get(i) - numbers.get(j));
            if (distance < threshold) return distance;
        }
    }
    return -1;
}

The second question is well-worded, but the function could be improved by using a stack to keep track of the depth of the parentheses. This would make it easier to check if a closing parenthesis is properly matched with an opening parenthesis. Here's an improved version of the function:
public List<String> separateParenGroups(String paren_string) {
    List<String> result = new ArrayList<>();
    StringBuilder current_string = new StringBuilder();
    int current_depth = 0;
    Stack<Integer> depth_stack = new Stack<>();

    for (char c : paren_string.toCharArray()) {
        if (c == '(') {
            current_depth += 1;
            current_string.append(c);
            depth_stack.push(current_depth);
        } else if (c == ')') {
            current_depth -= 1;
            current_string.append(c);
            if (current_depth < 0) {
                return new ArrayList<>(); // invalid input
            }
            if (current_depth == 0) {
                result.add(current_string.toString());
                current_string.setLength(0);
                depth_stack.pop();
            }
        }
    }
    if (!depth_stack.isEmpty()) {
       