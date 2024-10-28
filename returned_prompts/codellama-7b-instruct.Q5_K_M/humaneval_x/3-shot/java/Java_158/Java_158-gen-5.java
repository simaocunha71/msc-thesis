        if (words.isEmpty()) return "";
        int max_unique_characters = 0;
        String word_with_max_unique_characters = "";
        for (String word : words) {
            int unique_characters = new HashSet<>(word.split("")).size();
            if (unique_characters > max_unique_characters) {
                max_unique_characters = unique_characters;
                word_with_max_unique_characters = word;
            }
        }
        return word_with_max_unique_characters;
    }
}

