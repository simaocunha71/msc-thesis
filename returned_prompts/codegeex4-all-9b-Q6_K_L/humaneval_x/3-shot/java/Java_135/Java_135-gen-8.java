
Solution A: hasCloseElements
Your solution is correct. There are some minor style improvements that could be made.

You use a for-each loop, but you really want a traditional for loop so you can index the list.
You don't need to cast the result of get() to Double because it's already a Double.
You don't need to use Math.abs, because you're taking the absolute value of a Double.

Here's a cleaned-up version of your solution:
public boolean hasCloseElements(List<Double> numbers, double threshold) {
    for (int i = 0; i < numbers.size(); i++) {
        for (int j = i + 1; j < numbers.size(); j++) {
            double distance = numbers.get(i) - numbers.get(j);
            if (distance < threshold) return true;
        }
    }
    return false;
}

Solution A: separateParenGroups
Your solution is correct, but it could be cleaned up a little. The logic is fine, but the code could be more concise.

You don't need to use StringBuilder to build your string. You can just append the character directly to the current_string.
You don't need to use setLength(0) to clear the StringBuilder. You can just assign an empty string to it.
You don't need to use charAt() to get the character at a specific index. You can just use the char type directly.
You don't need to use toCharArray() to convert a string to a character array. You can just use the char type directly.

Here's a cleaned-up version of your solution:
public List<String> separateParenGroups(String paren_string) {
    List<String> result = new ArrayList<>();
    String current_string = "";
    int current_depth = 0;

    for (char c : paren_string.toCharArray()) {
        if (c == '(') {
            current_depth += 1;
            current_string += c;
        } else if (c == ')') {
            current_depth -= 1;
            current_string += c;

            if (current_depth == 0) {
                result.add(current_string);
                current_string = "";
            }
        }
    }
    return result;
}

Solution A: truncateNumber
Your solution is correct, but it could