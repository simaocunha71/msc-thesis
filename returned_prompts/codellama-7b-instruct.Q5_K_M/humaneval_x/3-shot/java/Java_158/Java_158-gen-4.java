        if (words.size() == 1) return words.get(0);

        Map<Character, Integer> char_freq = new HashMap<>();
        int max_freq = 0;
        String result = "";

        for (String word : words) {
            if (word.length() > max_freq) {
                max_freq = word.length();
                result = word;
            } else if (word.length() == max_freq) {
                int i = 0;
                for (; i < word.length(); i++) {
                    if (!char_freq.containsKey(word.charAt(i))) {
                        char_freq.put(word.charAt(i), 0);
                    }
                    char_freq.put(word.charAt(i), char_freq.get(word.charAt(i)) + 1);
                }
                for (int j = 0; j < word.length(); j++) {
                    if (char_freq.get(word.charAt(j)) > 1) {
                        break;
                    }
                    if (j == word.length() - 1) {
                        result = word;
                    }
                }
            }
        }
        return result;
    }
}

