    public Object splitWords(String txt) {
        if (txt.matches("^[a-zA-Z]+$")) {
            int count = 0;
            for (char c : txt.toCharArray()) {
                if ((c - 'a') % 2 != 0) {
                    count++;
                }
            }
            return count;
        } else {
            String[] words = txt.split("\\s+|,");
            return Arrays.asList(words);
        }
    }  // 1. Split the string on whitespace and commas. If no whitespaces or commas are present, split on lowercase letters with odd order in the alphabet. 2. The output should be a list of words if the input contains whitespaces or commas, otherwise the count of lowercase letters with odd order in the alphabet.
    // In Java, the split() method of the String class can be used to split a string into an array of strings. It takes a regular expression as an argument, and splits the string at each occurrence of the regular expression. The regular expression "\\s+|," in this case, matches one or more whitespace characters or a comma.  // The toCharArray() method of the String class can be used to convert a string into a character array. The for-each loop in the code iterates over the character array, and for each character, it checks whether the character is a lowercase letter with odd order in the alphabet by subtracting the ASCII value of 'a' from the ASCII value of the character. If the result is not zero, it means the character is a lowercase letter with odd order in the alphabet, and the count is incremented. The count is then returned as the result.  // If the input string does not contain any whitespaces or commas, the split() method will return an array with a single element, which is the original string. In this case, the code checks whether the string matches the regular expression "^[a-zA-Z]+$", which matches a string that contains only lowercase and uppercase letters. If the string matches this regular expression, it means the string does not contain any whitespaces or commas, and the code returns the count of lowercase letters with odd order in the alphabet. Otherwise, the code returns the array of strings.  // The code uses the Arrays.asList() method to convert the array of strings to a list of strings. The Arrays.asList() method is a static method of the Arrays class, and it returns a list view of the specified array.  // The code also uses the matches() method of