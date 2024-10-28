        String[] validExtensions = {"txt", "exe", "dll"};
        int countDigits = 0;
        boolean containsDot = false;
        boolean startsWithLetter = false;
        boolean validExtension = false;

        // Check the conditions
        for (int i = 0; i < file_name.length(); i++) {
            char c = file_name.charAt(i);
            if (Character.isDigit(c)) {
                countDigits++;
                if (countDigits > 3) {
                    return "No";
                }
            }
            if (c == '.') {
                containsDot = true;
            }
            if (i == 0 && Character.isLetter(c)) {
                startsWithLetter = true;
            }
            if (i > 0 && (c == '.' || i == file_name.length() - 1) && Character.isLetter(file_name.charAt(i - 1))) {
                for (String extension : validExtensions) {
                    if (file_name.substring(i + 1).equals(extension)) {
                        validExtension = true;
                    }
                }
            }
        }

        // If all conditions are met, return "Yes"
        if (countDigits <= 3 && containsDot && startsWithLetter && validExtension) {
            return "Yes";
        }

        // Otherwise, return "No"
        return "No";
    }
}

This solution works by iterating over each character in the file name and checking if it meets the specified conditions. If a character fails a condition, the function immediately returns "No". If all characters pass the conditions, the function returns "Yes".

Note: This solution assumes that the file name does not contain any spaces or special characters. If this is not the case, you would need to add additional checks to ensure that the file name is valid.

Also note that this solution uses the `String.substring(int)` method to check the file's extension. This method returns a new string that is a substring of this string. The substring begins with the character at the specified index and extends to the end of this string. This means that the