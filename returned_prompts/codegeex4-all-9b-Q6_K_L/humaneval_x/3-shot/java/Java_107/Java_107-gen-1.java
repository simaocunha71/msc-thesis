
You've got good answers already, but I'd like to add some more details to them.
The first one is a good start, but you can reduce the complexity of your function by using a HashSet to store the numbers you've seen so far.  That way, you only need to iterate over the list once, which makes the function O(n) instead of O(n^2).  Here's how I'd write it:
public boolean hasCloseElements(List<Double> numbers, double threshold) {
    Set<Double> seen = new HashSet<>();

    for (Double number : numbers) {
        if (seen.contains(number - threshold) || seen.contains(number + threshold)) {
            return true;
        }
        seen.add(number);
    }
    return false;
}

The second one is also a good start, but you can make it a little more efficient by using a StringBuilder to build the string, and adding the groups to the result list as you go.  That way, you only need to iterate over the characters in the input string once, which makes the function O(n) instead of O(n^2).  Here's how I'd write it:
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

The third one is a good start, but you can make it a little more