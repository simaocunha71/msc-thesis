        String max_word = "";
        int max_unique = 0;

        for (String word : words) {
            Set<Character> unique_chars = new HashSet<>();
            for (char c : word.toCharArray()) {
                unique_chars.add(c);
            }

            if (unique_chars.size() > max_unique) {
                max_unique = unique_chars.size();
                max_word = word;
            }
        }
        return max_word;
    }
}

