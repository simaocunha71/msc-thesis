    public Object splitWords(String txt) {
        if (txt.isEmpty()) {
            return 0;
        }
        String[] words = txt.split("\\s+");
        if (words.length > 0) {
            return Arrays.asList(words);
        } else {
            return txt.replace(",", "").toLowerCase().chars().filter(c -> c >= 'a' && c <= 'z').filter(c -> (int) c - (int) 'a' % 2 == 1).count();
        }
    }
    // If the input string is empty, return 0.
    // Split the input string on whitespace, and if it results in more than one word, return the list of words.
    // If splitting on whitespace does not result in more than one word, split on commas. If this still does not result in more than one word, count the number of lowercase letters with odd order in the alphabet.
    // The function takes a string as input and returns a list of words or an integer. The integer represents the number of lowercase letters with odd order in the alphabet. The function is case insensitive. If the input string is empty, it returns 0. If the string contains only whitespace, it returns an empty list. If the string contains only commas, it returns a list with the string without commas. If the string contains both whitespace and commas, it returns a list of the words in the string. If the string contains no letters, it returns 0. If the string contains only uppercase letters, it returns 0. If the string contains lowercase letters with odd order in the alphabet, it returns the count of these letters. The function uses the ASCII values of characters to determine if a character is lowercase and if it has an odd order in the alphabet. The function also uses the split method of the string class to split the string on whitespace and commas. The function uses the filter method of the IntStream class to filter the characters in the string. The function uses the count method of the IntStream class to count the characters in the string. The function uses the toList method of the Stream class to convert the stream of characters to a list. The function uses the replace method of the string class to replace commas with empty strings. The function uses the toLowerCase method of the string class to convert the string to lowercase. The function uses the chars method of the string class to convert the string to a stream of characters. The function uses the filter method of the IntStream class to filter the characters in the string