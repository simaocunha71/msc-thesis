        List<Integer> unique_chars = new ArrayList<>();
        int max_length = 0;
        String result = "";

        for (String word : words) {
            unique_chars.clear();

            for (char c : word.toCharArray()) {
                if (unique_chars.contains(c)) continue;
                unique_chars.add(c);
            }
            if (unique_chars.size() > max_length) {
                result = word;
                max_length = unique_chars.size();
            } else if (unique_chars.size() == max_length && result.compareTo(word) > 0) {
                result = word;
            }
        }
        return result;
    }
}

