        String max_word = "";
        int max_unique_chars = 0;

        for (String word : words) {
            int unique_chars = 0;
            Set<Character> unique_chars_set = new HashSet<>();

            for (char c : word.toCharArray()) {
                if (unique_chars_set.add(c)) unique_chars += 1;
            }

            if (unique_chars > max_unique_chars) {
                max_unique_chars = unique_chars;
                max_word = word;
            } else if (unique_chars == max_unique_chars) {
                max_word = minLex(word, max_word);
            }
        }
        return max_word;
    }

    private String minLex(String a, String b) {
        if (a.length() == b.length()) return a.compareTo(b) < 0 ? a : b;
        else return a.length() < b.length() ? a : b;
    }
}

