        // Check if there are more than three digits in the file's name
        int countDigits = 0;
        for (char c : file_name.toCharArray()) {
            if (Character.isDigit(c)) {
                countDigits++;
            }
        }
        if (countDigits > 3) {
            return "No";
        }

        // Check if there is exactly one dot in the file's name
        int countDots = 0;
        for (char c : file_name.toCharArray()) {
            if (c == '.') {
                countDots++;
            }
        }
        if (countDots != 1) {
            return "No";
        }

        // Check if the substring before the dot starts with a latin alphapet letter
        if (!Character.isLetter(file_name.charAt(0))) {
            return "No";
        }

        // Check if the substring after the dot is one of these: ["txt", "exe", "dll"]
        String[] validExtensions = {"txt", "exe", "dll"};
        String extension = file_name.substring(file_name.lastIndexOf(".") + 1);
        if (!Arrays.asList(validExtensions).contains(extension)) {
            return "No";
        }

        return "Yes";
    }
}

This solution checks if the file name is valid based on the conditions you provided. It counts the digits, dots and checks if the file name starts with a letter. It also checks if the file extension is one of the valid extensions.

In the code, `Character.isDigit(c)` checks if a character is a digit, `Character.isLetter(c)` checks if a character is a letter, and `Arrays.asList(array).contains(object)` checks if an array contains an object.

In the `filenameCheck` method, `file_name.charAt(0)` gets the first character of the file name, `file_name.substring(startIndex, endIndex)` gets a substring from the file name, and `file_name.lastIndexOf