        String max = "";
        int max_len = 0;

        for (String word : words) {
            Set<Character> unique_chars = new HashSet<>();

            for (char c : word.toCharArray()) {
                unique_chars.add(c);
            }

            if (unique_chars.size() > max_len) {
                max = word;
                max_len = unique_chars.size();
            } else if (unique_chars.size() == max_len) {
                max = max.compareTo(word) < 0 ? max : word;
            }
        }

        return max;
    }
}

