        int max_count = -1;
        String max_word = "";
        for (String word : words) {
            Set<Character> chars = new HashSet<>();
            for (char c : word.toCharArray()) {
                chars.add(c);
            }
            if (chars.size() > max_count) {
                max_count = chars.size();
                max_word = word;
            } else if (chars.size() == max_count && word.compareTo(max_word) < 0) {
                max_word = word;
            }
        }
        return max_word;
    }
}

