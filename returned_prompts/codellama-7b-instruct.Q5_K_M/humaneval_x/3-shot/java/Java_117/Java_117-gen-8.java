        List<String> result = new ArrayList<>();
        if (s.length() == 0) return result;
        int word_start = 0;
        int word_end = 0;
        while (word_end < s.length()) {
            if (s.charAt(word_end) != ' ') {
                word_end += 1;
            } else {
                String word = s.substring(word_start, word_end);
                word_start = word_end + 1;
                int count = 0;
                for (char c : word.toCharArray()) {
                    if (Character.isAlphabetic(c) && !Character.isUpperCase(c)) count += 1;
                }
                if (count == n) result.add(word);
            }
        }
        return result;
    }
}

