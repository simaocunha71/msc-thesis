
for (int i = 0; i < numbers.size(); i++) {
    for (int j = i + 1; j < numbers.size(); j++) {
        double distance = Math.abs(numbers.get(i) - numbers.get(j));
        if (distance < threshold) return true;
    }
}
return false;

This is a good implementation of the problem, it simply checks all pairs of numbers and sees if the distance is less than the threshold.

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

This is a good implementation of the problem, it simply counts the depth of the parentheses and when it reaches 0 it adds the string to the result.

public double truncateNumber(double number) {

    return number % 1.0;
}

This is a good implementation of the problem, it simply returns the remainder of the number divided by 1.

public double poly(List<Double> xs, double x) {
    double result = 0;
    for (int i = 0; i < xs.size(); i++) {
        result += xs.get(i) * Math.pow(x, i);
    }
    return result;
}

This is a good implementation of the problem, it simply sums up all the terms of the polynomial.

public double findZero(List<Double> xs) {

    double a = 1.0;
    double b = -xs.get(xs.size() - 1) / xs.get(xs.size() - 2);
    while (Math.abs(a - b) > 1