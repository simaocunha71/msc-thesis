    public String filenameCheck(String file_name) {
        String[] fileExtensions = {"txt", "exe", "dll"};
        int countDigits = 0;
        boolean hasDot = false;
        String beforeDot = "";
        String afterDot = "";

        for (int i = 0; i < file_name.length(); i++) {
            char ch = file_name.charAt(i);
            if (Character.isDigit(ch)) {
                countDigits++;
            }
            if (ch == '.') {
                hasDot = true;
                beforeDot = file_name.substring(0, i);
                afterDot = file_name.substring(i + 1);
            }
        }

        if (countDigits > 3 || !hasDot || beforeDot.isEmpty() || !isLatinLetter(beforeDot.charAt(0)) || !isExtensionValid(afterDot)) {
            return "No";
        } else {
            return "Yes";
        }
    }

    private boolean isLatinLetter(char ch) {
        return (ch >= 'a' && ch <= 'z') || (ch >= 'A' && ch <= 'Z');
    }

    private boolean isExtensionValid(String extension) {
        for (String fileExtension : {"txt", "exe", "dll"}) {
            if (fileExtension.equals(extension)) {
                return true;
            }
        }
        return false;
    }  // end of Solution class

Here's a breakdown of the solution:

1.  We define a function `filenameCheck` that takes a string `file_name` as input.
2.  We initialize several variables: `countDigits` to count the number of digits in the file name, `hasDot` to track whether the file name contains a dot, `beforeDot` to store the substring before the dot, and `afterDot` to store the substring after the dot.
3.  We iterate through each character `ch` in the `file_name` using a for loop.
4.  If `ch` is a digit, we increment `countDigits`.
5.  If `ch` is a dot, we set `hasDot` to `true` and extract the substrings `beforeDot` and `afterDot`.
6.  We then check if the file name is valid based on the conditions:
    *   If `countDigits` is greater than 3, the file name is invalid.
    *   If `hasDot` is `false`, the file name is invalid.
    *   If `