
For the first question, you can make it more readable by using a for-each loop instead of a traditional for loop:
public boolean hasCloseElements(List<Double> numbers, double threshold) {
    for (double num : numbers) {
        for (double other : numbers) {
            if (num != other && Math.abs(num - other) < threshold) {
                return true;
            }
        }
    }
    return false;
}

The second question can be simplified by using a stack to keep track of the current depth, instead of using a StringBuilder and an integer. This will also make it easier to handle malformed input:
public List<String> separateParenGroups(String paren_string) {
    List<String> result = new ArrayList<>();
    int current_depth = 0;
    StringBuilder current_string = new StringBuilder();

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

The third question can be simplified by using a Math.floor() call instead of the modulo operator:
public double truncateNumber(double number) {
    return number - Math.floor(number);
}

The fourth question can be simplified by using a Comparator to sort the list in ascending order:
public List<Integer> sortArray(List<Integer> array) {
    List<Integer> copy = new ArrayList<>(array);
    copy.sort(Comparator.comparingInt(o -> o));
    return copy;
}