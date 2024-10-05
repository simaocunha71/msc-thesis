        Map<Character, Integer> char_count = new HashMap<>();
        String max_word = "";
        int max_count = 0;

        for (String word : words) {
            char_count.clear();
            int count = 0;

            for (char c : word.toCharArray()) {
                if (char_count.containsKey(c)) {
                    char_count.put(c, char_count.get(c) + 1);
                } else {
                    char_count.put(c, 1);
                    count += 1;
                }
            }
            if (count > max_count) {
                max_count = count;
                max_word = word;
            } else if (count == max_count && max_word.compareTo(word) > 0) {
                max_word = word;
            }
        }
        return max_word;
    }
}

