    public Object splitWords(String txt) {
        String[] words = txt.split("\\s+"); // split on one or more whitespace characters
        if (words.length == 0) {
            words = txt.split(","); // split on commas if no whitespace found
            if (words.length == 0) {
                int count = 0;
                for (char c : txt.toLowerCase().toCharArray()) {
                    if ((c - 'a' % 26) % 2 == 1) {
                        count++;
                    }
                }
                return count;
            }
        }
        return Arrays.asList(words);
    }  // Return a list of words split on whitespace, if no whitespaces exists in the text you should split on commas ',' if no commas exists you should return the number of lower-case letters with odd order in the alphabet, ord('a') = 0, ord('b') = 1, ... ord('z') = 25
} // End of Solution class.  // End of Solution class.