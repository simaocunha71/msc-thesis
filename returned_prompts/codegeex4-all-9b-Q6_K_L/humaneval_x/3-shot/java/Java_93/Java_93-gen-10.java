
Your first solution is fine. I think it can be improved with a single line return statement. Here's how you could write it:
public boolean hasCloseElements(List<Double> numbers, double threshold) {
    return numbers.stream()
                   .anyMatch(n -> numbers.stream()
 .anyMatch(m -> m != n && Math.abs(n - m) < threshold));
}

Your second solution is fine. I think it can be improved with a single line return statement. Here's how you could write it:
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

Your third solution can be improved by using the Math.floor function which will always return a double value that is less than or equal to