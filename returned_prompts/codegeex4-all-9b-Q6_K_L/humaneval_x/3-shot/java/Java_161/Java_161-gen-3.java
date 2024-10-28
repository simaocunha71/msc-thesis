
I'll start with the last one, since it's the easiest:

public String solve(String s) {
    StringBuilder result = new StringBuilder();

    for (char c : s.toCharArray()) {
        if (Character.isLetter(c)) {
            if (Character.isUpperCase(c)) {
                result.append(Character.toLowerCase(c));
            } else {
                result.append(Character.toUpperCase(c));
            }
        } else {
            result.append(c);
        }
    }
    return result.reverse().toString();
}

This one is good, but you can get rid of the else statement, since you're just reversing the string anyway:
public String solve(String s) {
    StringBuilder result = new StringBuilder();

    for (char c : s.toCharArray()) {
        if (Character.isLetter(c)) {
            result.append(Character.isUpperCase(c) ? Character.toLowerCase(c) : Character.toUpperCase(c));
        } else {
            result.append(c);
        }
    }
    return result.reverse().toString();
}

Next, the one with the floating point numbers:

public double truncateNumber(double number) {
    return number % 1.0;
}

This one is also good, but you can make it a bit more readable by using Math.floor() instead of the modulus operation:
public double truncateNumber(double number) {
    return number - Math.floor(number);
}

And the one with the parentheses:

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

This one is also good, but you can make it a bit more readable by using a while loop instead of the for loop:
public List<String> separateParenGroups