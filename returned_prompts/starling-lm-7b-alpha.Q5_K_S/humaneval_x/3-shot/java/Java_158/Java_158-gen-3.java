        int max_count = 0;
        String result = "";
        for (String word : words) {
            Set<Character> unique_chars = new HashSet<>();
            for (char c : word.toCharArray()) {
                unique_chars.add(c);
            }
            if (unique_chars.size() > max_count) {
                max_count = unique_chars.size();
                result = word;
            } else if (unique_chars.size() == max_count) {
                if (result.compareTo(word) > 0) {
                    result = word;
                }
            }
        }
        return result;
    }
}

