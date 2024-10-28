        int last_index = txt.length() - 1;
        if (last_index < 0) return false;

        char last_char = txt.charAt(last_index);
        boolean is_word_separator = Character.isWhitespace(last_char);
        boolean is_alphabetical = Character.isLetter(last_char);

        return !is_word_separator && is_alphabetical;
    }
}

