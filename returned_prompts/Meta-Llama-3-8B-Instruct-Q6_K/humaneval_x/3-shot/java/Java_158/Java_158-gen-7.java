        String max_word = "";
        int max_length = 0;

        for (String word : words) {
            Set<Character> set = new HashSet<>();
            for (char c : word.toCharArray()) {
                set.add(c);
            }

            if (set.size() > max_length) {
                max_word = word;
                max_length = set.size();
            }
        }

        return max_word;
    }
} 