Here is a Java function that checks if a file name is valid according to the given conditions:

```java
public String filenameCheck(String file_name) {
    String[] extensions = {"txt", "exe", "dll"};
    if (file_name.length() > 0) {
        if (file_name.contains(".")) {
            String[] parts = file_name.split("\\.");
            if (parts.length == 2) {
                if (parts[0].matches("[a-zA-Z][a-zA-Z0-9]*")) {
                    if (Arrays.asList(extensions).contains(parts[1].toLowerCase())) {
                        int count = 0;
                        for (char c : parts[0].toCharArray()) {
                            if (Character.isDigit(c)) {
                                count++;
                            }
                            if (count > 3) {
                                return "No";
                            }
                        }
                        return "Yes";
                    } else {
                        return "No";
                    }
                } else {
                    return "No";
                }
            } else {
                return "No";
            }
        } else {
            return "No";
        }
    } else {
        return "No";
    }
}
```

This function checks if the file name contains a dot, if the part before the dot starts with a letter and contains only letters and digits, if the part after the dot is one of the allowed extensions, and if there are no more than three digits in the file name. If any of these conditions are not met, the function returns "No". Otherwise, it returns "Yes".  The function also converts the file name to lower case when checking the extension to make the check case-insensitive.  If the file name is empty, the function also returns "No".  The file name is split into two parts at the dot using the `split` method with a regular expression.  The `matches` method is used to check if the part before the dot starts with a letter and contains only letters and digits.  The `contains` method is used to check if the part after the dot is one of the allowed extensions.  The `Arrays.asList` method is used to convert the array of extensions to a list, and the `contains` method is used to check if the list contains the part after the dot.  The `Character.isDigit` method is used to check if a character is a digit, and the `count` variable is used to count the number of digits in the part before the dot.  If the count exceeds