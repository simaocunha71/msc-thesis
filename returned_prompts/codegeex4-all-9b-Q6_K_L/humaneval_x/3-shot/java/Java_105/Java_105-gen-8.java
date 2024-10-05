
hasCloseElements
The code does exactly what is asked for, and is efficient. However, there are a few things to improve:

It is better to use a for-each loop with the index variable, as it is more readable:
for (int i = 0; i < numbers.size(); i++) {
    for (int j = i + 1; j < numbers.size(); j++) {
        // ...
    }
}

The naming of the variables can be improved. For example, current_string can be renamed to current_group, and current_depth to group_depth.
The StringBuilder can be replaced by a String, as it is not needed:
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

The StringBuilder is replaced by a String, as it is not needed:
String current_group = "";
int group_depth = 0