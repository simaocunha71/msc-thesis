        int max_unique_chars = 0;
        String result = "";

        for (String word : words) {
            int unique_chars = uniqueChars(word);
            if (unique_chars > max_unique_chars) {
                max_unique_chars = unique_chars;
                result = word;
            } else if (unique_chars == max_unique_chars) {
                if (result.compareTo(word) > 0) {
                    result = word;
                }
            }
        }
        return result;
    }

    // count the number of unique characters in given string
    private int uniqueChars(String word) {
        Set<Character> chars = new HashSet<>();
        for (char c : word.toCharArray()) {
            chars.add(c);
        }
        return chars.size();
    }
}

