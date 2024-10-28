        Map<Character, Integer> unique_chars = new HashMap<>();
        String result = "";
        int max_unique_chars = 0;

        for (String word : words) {
            unique_chars.clear();

            for (char c : word.toCharArray()) {
                if (!unique_chars.containsKey(c)) {
                    unique_chars.put(c, 1);
                } else {
                    int count = unique_chars.get(c) + 1;
                    unique_chars.put(c, count);
                }
            }

            if (unique_chars.size() > max_unique_chars ||
                (unique_chars.size() == max_unique_chars && word.compareTo(result) < 0)) {
                result = word;
                max_unique_chars = unique_chars.size();
            }

        }

        return result;
    }
}

