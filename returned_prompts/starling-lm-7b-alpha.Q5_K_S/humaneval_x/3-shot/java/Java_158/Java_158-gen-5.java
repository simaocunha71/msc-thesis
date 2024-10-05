        int max_count = Integer.MIN_VALUE;
        String max_word = "";
        for (String word : words) {
            Set<Character> char_set = new HashSet<>();
            for (char c : word.toCharArray()) {
                char_set.add(c);
            }
            if (char_set.size() > max_count) {
                max_count = char_set.size();
                max_word = word;
            }
        }
        return max_word;
    }
}

