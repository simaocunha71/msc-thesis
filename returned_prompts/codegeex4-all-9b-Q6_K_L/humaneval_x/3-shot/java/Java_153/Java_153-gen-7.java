
Your first piece of code is correct and efficient. The time complexity is O(n^2) which is fine for this problem since the list is at most 1000 elements long.
Your second piece of code is correct, but it can be made more efficient by using a stack to keep track of the current depth of parentheses. This way, you don't have to keep track of the current depth as you iterate through the characters.
Here's the improved version:
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

Your third piece of code is correct, but it can be made more efficient by using the Math.floor() function to truncate the number. This way, you don't have to use the modulus operator.
Here's the improved version:
public double truncateNumber(double number) {
    return Math.floor(number);
}

Your fourth piece of code is correct, but it can be made more efficient by using a map to keep track of the strength of each extension. This way, you don't have to iterate through all the extensions to find the strongest one.
Here's the improved version:
public String StrongestExtension(String class_name, List<String> extensions) {
    Map<String, Double> strengths = new HashMap<>();
    String strongest = extensions.get(0);
    double strength = 0.0;

    for (String ext : extensions) {
        int cap