
hasCloseElements
The algorithm is correct, but can be simplified. You don't need the inner loop to go from i + 1 to size(), you can just go from 0 to size(). The algorithm also doesn't need to store the distance, you can just compare directly:
public boolean hasCloseElements(List<Double> numbers, double threshold) {
    for (int i = 0; i < numbers.size(); i++) {
        for (int j = 0; j < numbers.size(); j++) {
            if (i != j && Math.abs(numbers.get(i) - numbers.get(j)) < threshold) return true;
        }
    }
    return false;
}

separateParenGroups
The current_depth is only used to detect when the current group is closed, so there is no need to keep track of it. You can just increment it on every open parenthesis and decrement it on every close parenthesis. When it reaches 0, you know you've closed a group:
public List<String> separateParenGroups(String paren_string) {
    List<String> result = new ArrayList<>();
    StringBuilder current_string = new StringBuilder();

    for (char c : paren_string.toCharArray()) {
        if (c == '(') {
            current_string.append(c);
        } else if (c == ')') {
            current_string.append(c);
            if (current_string.charAt(current_string.length() - 2) == '(') {
                current_string.deleteCharAt(current_string.length() - 1);
                current_string.deleteCharAt(current_string.length() - 1);
                result.add(current_string.toString());
                current_string.setLength(0);
            }
        }
    }
    return result;
}

truncateNumber
The algorithm is correct, but you can simplify it by using the BigDecimal class:
public double truncateNumber(double number) {
    return BigDecimal.valueOf(number).stripTrailingZeros().doubleValue();
}

fizzBuzz
The algorithm is correct, but you can simplify it by using the modulo operator:
public int fizzBuzz(int n) {
    int count = 0;
    for (