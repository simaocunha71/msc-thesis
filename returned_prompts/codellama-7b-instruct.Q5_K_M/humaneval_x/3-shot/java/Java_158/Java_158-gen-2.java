        Map<Character, Integer> char_count = new HashMap<>();
        String max_word = "";
        int max_chars = 0;

        for (String word : words) {
            char_count.clear();
            for (char c : word.toCharArray()) {
                if (char_count.containsKey(c)) {
                    char_count.put(c, char_count.get(c) + 1);
                } else {
                    char_count.put(c, 1);
                }
            }
            if (char_count.size() > max_chars) {
                max_chars = char_count.size();
                max_word = word;
            } else if (char_count.size() == max_chars) {
                if (max_word.compareTo(word) > 0) {
                    max_word = word;
                }
            }
        }
        return max_word;
    }
}

