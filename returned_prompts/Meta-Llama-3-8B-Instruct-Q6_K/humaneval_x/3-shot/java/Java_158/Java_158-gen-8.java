        String result = "";
        int max_unique_chars = 0;

        for (String word : words) {
            Set<Character> unique_chars = new HashSet<>();
            for (char c : word.toCharArray()) {
                unique_chars.add(c);
            }
            if (unique_chars.size() > max_unique_chars) {
                max_unique_chars = unique_chars.size();
                result = word;
            }
        }
        return result;
    }
}

