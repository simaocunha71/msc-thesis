
Your first function is fine, just a small change:
public boolean hasCloseElements(List<Double> numbers, double threshold) {
    for (int i = 0; i < numbers.size(); i++) {
        for (int j = i + 1; j < numbers.size(); j++) {
            double distance = Math.abs(numbers.get(i) - numbers.get(j));
            if (distance <= threshold) return true;
        }
    }
    return false;
}

You seem to have forgotten the equals operator. The two numbers are close if their distance is less than or equal to the threshold, not just less than.
Your second function is also fine, just a small change:
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

You seem to have forgotten to add the closing brace to the current_string. You only append the opening brace.
Your third function is also fine, just a small change:
public double truncateNumber(double number) {
    return number % 1.0;
}

You seem to have forgotten the equals operator. The number is truncated if its remainder when divided by 1.0 is 0.0, not just less than 1.0.