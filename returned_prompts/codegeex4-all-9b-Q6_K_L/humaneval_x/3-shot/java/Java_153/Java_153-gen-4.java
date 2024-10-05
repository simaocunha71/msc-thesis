
Your code has a logical error in the second question. You should not remove the last character from current_string when current_depth is 0, because you still need that character to close the parentheses.
To fix this, you can modify your code as follows:
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

In the third question, you can simplify your code by using the Math.floor() function to truncate the number. This function returns the largest integer less than or equal to the given number. For example, Math.floor(3.5) returns 3.
Here is the simplified code:
public double truncateNumber(double number) {
    return Math.floor(number);
}

In the fourth question, your code is correct. You correctly calculate the strength of each extension and choose the strongest one. However, you can simplify your code by using the String.toUpperCase() and String.toLowerCase() methods to count the number of uppercase and lowercase letters in each extension. Here is the simplified code:
public String StrongestExtension(String class_name, List<String> extensions) {
    String strongest_extension = extensions.get(0);
    int strongest_strength = 0;

    for (String extension : extensions) {
        int cap = extension.toUpperCase().length();
        int sm = extension.toLowerCase().length();

        int strength = cap - sm;

        if (strength > strongest_strength) {
            strongest