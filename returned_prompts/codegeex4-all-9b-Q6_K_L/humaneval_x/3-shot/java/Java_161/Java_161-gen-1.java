
Q1: Check if in given list of numbers, are any two numbers closer to each other than given threshold.
A1:
public boolean hasCloseElements(List<Double> numbers, double threshold) {
    for (int i = 0; i < numbers.size(); i++) {
        for (int j = i + 1; j < numbers.size(); j++) {
            double distance = Math.abs(numbers.get(i) - numbers.get(j));
            if (distance < threshold) return true;
        }
    }
    return false;
}

This solution is correct, but it can be optimized. We can sort the list of numbers first, and then iterate through the list once, checking if the difference between consecutive numbers is less than the threshold.

Q2: Input to this function is a string containing multiple groups of nested parentheses. Your goal is to separate those group into separate strings and return the list of those.
A2:
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

This solution is correct, but it can be optimized. We can use a stack to keep track of the current depth of parentheses, and push and pop elements from the stack as we encounter parentheses. When the current depth of parentheses becomes 0, we know that we have reached the end of a group of parentheses, and we can add the group to the result list.

Q3: Given a positive floating point number, it can be decomposed into and integer part (largest integer smaller than given number) and decimals (leftover part always smaller than 1). Return the decimal part of the number.
A3:
public double