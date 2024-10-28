        String max_word = null;
        int max_length = 0;

        for (String word : words) {
            int length = word.length();
            int unique_chars = word.chars().distinct().count();

            if (length > max_length || (length == max_length && word.compareTo(max_word) < 0)) {
                max_word = word;
                max_length = length;
            }
        }
        return max_word;
    }
}

