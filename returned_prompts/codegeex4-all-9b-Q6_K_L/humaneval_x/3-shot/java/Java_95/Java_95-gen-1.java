
You are missing closing braces for the methods. They should look like this:
public boolean hasCloseElements(List<Double> numbers, double threshold) {
    for (int i = 0; i < numbers.size(); i++) {
        for (int j = i + 1; j < numbers.size(); j++) {
            double distance = Math.abs(numbers.get(i) - numbers.get(j));
            if (distance < threshold) return true;
        }
    }
    return false;
}

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

public double truncateNumber(double number) {
    return number % 1.0;
}

public boolean checkDictCase(Map<Object, Object> dict) {
    boolean all_upper = true;
    boolean all_lower = true;

    for (Object key : dict.keySet()) {
        if (!(key instanceof String)) return false;

        String string_key = (String) key;
        if (!string_key.equals(string_key.toUpperCase())) all_upper = false;
        if (!string_key.equals(string_key.toLowerCase())) all_lower = false;
    }
    return all_lower || all_upper;
}