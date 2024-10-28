        String max_word = words.get(0);
        int max_unique_chars = max_word.length();
        for (String word : words) {
            if (word.length() > max_unique_chars) {
                max_unique_chars = word.length();
                max_word = word;
            }
        }
        return max_word;
    }
}

