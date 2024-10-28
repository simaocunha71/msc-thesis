
hasCloseElements
Your solution is correct, but you could improve the performance a little bit by sorting the list before iterating. This way you can break the inner loop early when you know that the remaining values can't be closer than the threshold:
public boolean hasCloseElements(List<Double> numbers, double threshold) {
    numbers.sort(null);
    for (int i = 0; i < numbers.size() - 1; i++) {
        if (numbers.get(i + 1) - numbers.get(i) < threshold) {
            return true;
        }
    }
    return false;
}

separateParenGroups
Your solution is correct, but you could improve the readability a little bit by using a StringBuilder to build the current string:
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
Your solution is correct, but you could improve the readability a little bit by using Math.floorMod instead of the modulo operator:
public double truncateNumber(double number) {
    return Math.floorMod(number, 1.0);
}

xOrY
Your solution is correct, but you could improve the performance a little bit by using a more efficient algorithm to check if a number is prime:
public int xOrY(int n, int x, int y) {
    if (n <= 1) {
        return y;
    }
    for (int i = 2; i * i <= n; i++) {
        if (n % i == 0) {
            return y;
        }
    }
    return x;
}