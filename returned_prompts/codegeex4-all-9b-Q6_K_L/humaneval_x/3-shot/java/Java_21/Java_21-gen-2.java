
hasCloseElements
The algorithm is correct, but you can avoid the nested loop by using a TreeSet which will automatically order the numbers and make it easy to find the difference between the current number and the next one. This will also avoid the need for Math.abs. The only downside is that this will consume more memory, since you have to store all numbers in a TreeSet.
public boolean hasCloseElements(List<Double> numbers, double threshold) {
    if (numbers.size() < 2) return false;
    Set<Double> ordered = new TreeSet<>(numbers);
    Double last = null;
    for (Double number : ordered) {
        if (last != null && number - last < threshold) return true;
        last = number;
    }
    return false;
}

separateParenGroups
The code is correct, but it can be improved by removing the StringBuilder and using a String directly. This will also make it easier to debug.
public List<String> separateParenGroups(String paren_string) {
    List<String> result = new ArrayList<>();
    int current_depth = 0;
    int last_start = 0;
    for (int i = 0; i < paren_string.length(); i++) {
        char c = paren_string.charAt(i);
        if (c == '(') {
            current_depth += 1;
        } else if (c == ')') {
            current_depth -= 1;
            if (current_depth == 0) {
                result.add(paren_string.substring(last_start, i + 1));
                last_start = i + 1;
            }
        }
    }
    return result;
}

truncateNumber
The code is correct, but it can be improved by using Math.floor to get the integer part of the number. This will avoid the need for the cast to double.
public double truncateNumber(double number) {
    return number - Math.floor(number);
}

rescaleToUnit
The code is correct, but it can be improved by using the Stream API to make it more concise. This will also make it easier to read and maintain.
public List<Double> rescaleToUnit(List<Double> numbers) {
    double min = Collections.min(numbers);
    double max = Collections.max(numbers);
    return