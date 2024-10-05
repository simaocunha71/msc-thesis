
The first and last questions are quite simple and I will not comment on them. 

The second question, separateParenGroups, is not correct. If you look at the example, you will find that "()" and "(())" are not separated, but they are. This is because there is a space in between them. You should remove the space before adding it to the list. Here is the correct code:
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
                result.add(current_string.toString().trim());
                current_string.setLength(0);
            }
        }
    }
    return result;
}

The third question, truncateNumber, is not correct. You are using the modulus operator (%) to truncate the number, but this is not the correct way to do it. The modulus operator returns the remainder of a division operation, so it will not give you the decimal part of a number. You should use the Math.floor() function to truncate the number. Here is the correct code:
public double truncateNumber(double number) {
    return number - Math.floor(number);
}