        Map<Character, Integer> char_count = new HashMap<>();
        int max_count = 0;
        String max_word = "";

        for (String word : words) {
            char_count.clear();
            for (char c : word.toCharArray()) {
                char_count.put(c, char_count.getOrDefault(c, 0) + 1);
            }
            if (char_count.size() > max_count) {
                max_count = char_count.size();
                max_word = word;
            }
        }
        return max_word;
    }
}

