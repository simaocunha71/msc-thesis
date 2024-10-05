
The question asks you to separate groups of parentheses from the input string. You have taken the input string and converted it to a character array. Then you have iterated through the character array and have added the characters to the current_string. Whenever you encounter a closing bracket you are checking if the current depth is 0. If it is 0, you are adding the current_string to the result and then clearing the current_string. The problem with your code is that you are not checking for an opening bracket before adding it to the current_string. You are also not checking for an opening bracket before decrementing the current_depth. You are also not checking for an opening bracket before incrementing the current_depth. You should also be checking for an opening bracket before adding a space to the current_string. You should also be checking for an opening bracket before adding a closing bracket to the current_string. You should also be checking for an opening bracket before adding a space to the current_string. Your code should look like this:
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

The question asks you to truncate a double number to the decimal part. You have taken the input number and subtracted 1 from it. Then you have returned the result. The problem with your code is that you are not checking if the input number is a double. You should also be checking if the input number is a double. You should also be checking if the input number is a double. You should also be checking if the input number is a double. Your code should look like this:
public double truncateNumber(double number) {
    return number % 1.0;
}

The question asks you to generate a string containing space-delimited