        if (words.isEmpty()) return "";

        String max_word = words.get(0);
        int max_unique_chars = max_word.length();

        for (String word : words) {
            Set<Character> unique_chars = new HashSet<>();
            for (char c : word.toCharArray()) {
                unique_chars.add(c);
            }
            if (unique_chars.size() > max_unique_chars) {
                max_unique_chars = unique_chars.size();
                max_word = word;
            }
        }
        return max_word;
    }
}

