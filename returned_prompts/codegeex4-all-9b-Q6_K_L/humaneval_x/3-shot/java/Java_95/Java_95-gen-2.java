
Your for loops in the first code block are missing their braces. You need to add them to make it valid Java. For example:
for (int i = 0; i < numbers.size(); i++) {
    for (int j = i + 1; j < numbers.size(); j++) {
        double distance = Math.abs(numbers.get(i) - numbers.get(j));
        if (distance < threshold) return true;
    }
}

Also, when you add braces, you'll notice that you have an indentation problem in the same block. The line if (distance < threshold) return true; is indented like it's part of the for loop, but it's not. It should be indented like it's part of the if statement.
The second code block is missing a closing brace. It should look like this:
return result;
}

Your third code block has an off-by-one error in the for loop. The loop should go up to numbers.size() - 1, not numbers.size(). For example:
for (int i = 0; i < numbers.size() - 1; i++) {
    double distance = Math.abs(numbers.get(i) - numbers.get(i + 1));
    if (distance < threshold) return true;
}

The fourth code block has a few problems. First, the variable names are not descriptive enough. You should use more descriptive names, like "is_key_lower" and "is_key_upper". Second, you don't need to check if the key is an instance of String. Just check if it's a String. For example:
for (Map.Entry<Object, Object> entry : dict.entrySet()) {
    String key = (String) entry.getKey();
    if (!key.equals(key.toLowerCase())) is_lower = false;
    if (!key.equals(key.toUpperCase())) is_upper = false;
}