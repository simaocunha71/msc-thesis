
For the first question, you can do this in one pass:
public boolean hasCloseElements(List<Double> numbers, double threshold) {
    for (int i = 0; i < numbers.size() - 1; i++) {
        if (Math.abs(numbers.get(i) - numbers.get(i + 1)) < threshold) return true;
    }
    return false;
}

For the second question, you can do this in one pass:
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

For the third question, you can do this in one pass:
public double truncateNumber(double number) {
    return number % 1.0;
}

For the fourth question, you can do this in one pass:
public List<Integer> unique(List<Integer> l) {
    Set<Integer> set = new HashSet<>();
    for (Integer i : l) {
        set.add(i);
    }
    return new ArrayList<>(set);
}