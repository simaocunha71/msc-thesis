
hasCloseElements
The code in this method is correct, but inefficient.  It iterates over each pair of numbers twice, and only returns true if one of those pairs is within the threshold.  It is more efficient to iterate over each pair of numbers only once, and return true if any of those pairs is within the threshold.
public boolean hasCloseElements(List<Double> numbers, double threshold) {
    for (int i = 0; i < numbers.size(); i++) {
        for (int j = i + 1; j < numbers.size(); j++) {
            if (Math.abs(numbers.get(i) - numbers.get(j)) < threshold) {
                return true;
            }
        }
    }
    return false;
}

separateParenGroups
The code in this method is correct, but inefficient.  It uses a StringBuilder to build the current string, but then converts it to a String when it adds it to the result list.  This is unnecessary, and can be avoided by simply adding the char to the result list.
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

truncateNumber
The code in this method is correct, but inefficient.  It uses the modulus operator to find the decimal part of the number, but then converts it to a double.  This is unnecessary, and can be avoided by simply returning the result of the modulus operator.
public double truncateNumber(double number) {
    return number % 1.0