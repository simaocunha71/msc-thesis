        if (txt.isEmpty()) return false;

        boolean last_char_is_letter = false;
        boolean last_char_is_part_of_word = false;

        for (int i = txt.length() - 1; i >= 0; i--) {
            char c = txt.charAt(i);
            if (Character.isLetter(c)) {
                last_char_is_letter = true;
                break;
            }
            if (Character.isWhitespace(c)) break;
        }

        for (int i = txt.length() - 1; i >= 0; i--) {
            char c = txt.charAt(i);
            if (Character.isLetter(c)) {
                last_char_is_part_of_word = true;
                break;
            }
        }

        return last_char_is_letter && !last_char_is_part_of_word;
    }
}

