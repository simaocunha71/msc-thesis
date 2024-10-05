
For the first problem, you are doing an unnecessary check for the threshold, which should be >= 0.0. Also, you can use the Stream API in Java 8 to achieve the same result in a more elegant way.
public boolean hasCloseElements(List<Double> numbers, double threshold) {
    if (threshold < 0.0) {
        throw new IllegalArgumentException("threshold should be >= 0.0");
    }
    return numbers.stream()
                  .flatMap(n -> numbers.stream()
 .filter(m -> n != m)
 .map(m -> Math.abs(n - m)))
                  .anyMatch(d -> d < threshold);
}

For the second problem, you can simplify your code by removing the StringBuilder, and using a for-each loop to iterate over the characters in the string.
public List<String> separateParenGroups(String paren_string) {
    List<String> result = new ArrayList<>();
    int current_depth = 0;

    for (char c : paren_string.toCharArray()) {
        if (c == '(') {
            current_depth += 1;
        } else if (c == ')') {
            current_depth -= 1;

            if (current_depth == 0) {
                result.add(paren_string.substring(paren_string.lastIndexOf('('), paren_string.indexOf(')') + 1));
            }
        }
    }
    return result;
}

For the third problem, you are doing a division operation on the double number, which will result in a double value. You can simplify your code by using the Math.floor() method to get the integer part of the number.
public double truncateNumber(double number) {
    return number - Math.floor(number);
}

For the fourth problem, you can simplify your code by using the String.replaceAll() method to replace all consecutive spaces with a single underscore.
public String fixSpaces(String text) {
    return text.replaceAll("\\s+", "_");
}