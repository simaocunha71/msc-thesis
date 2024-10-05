        Map<Character, Integer> char_map = new HashMap<>();
        int max_unique_chars = 0;
        String result = "";
        for (String word : words) {
            char_map.clear();
            for (char c : word.toCharArray()) {
                if (char_map.containsKey(c)) {
                    char_map.put(c, char_map.get(c) + 1);
                } else {
                    char_map.put(c, 1);
                }
            }
            int unique_chars = char_map.size();
            if (unique_chars > max_unique_chars) {
                max_unique_chars = unique_chars;
                result = word;
            } else if (unique_chars == max_unique_chars && word.compareTo(result) < 0) {
                result = word;
            }
        }
        return result;
    }
}

