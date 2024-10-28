
The first question is correct. But the second question can be improved by using StringBuilder.
Here is the improved code:

```java
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
```

The third question can be improved by using the Math.floor() function.
Here is the improved code:

```java
public double truncateNumber(double number) {
    return number - Math.floor(number);
}
```

The fourth question can be improved by using the String.matches() method.
Here is the improved code:

```java
public String filenameCheck(String file_name) {
    String[] parts = file_name.split("\\.");
    if (parts.length != 2) return "No";
    if (parts[0].length() > 3) return "No";
    if (!parts[0].matches("[a-zA-Z].*")) return "No";
    if (!parts[1].matches("txt|exe|dll")) return "No";
    return "Yes";
}
```