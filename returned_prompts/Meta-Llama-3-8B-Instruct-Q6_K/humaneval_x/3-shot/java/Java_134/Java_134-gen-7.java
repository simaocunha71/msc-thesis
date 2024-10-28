        if (txt.isEmpty()) return false;

        String[] words = txt.split(" ");
        if (words.length == 0) return false;

        String last_word = words[words.length - 1];
        if (last_word.isEmpty()) return false;

        char last_char = last_word.charAt(last_word.length() - 1);
        return Character.isLetter(last_char) && !Character.isLetter(last_word.charAt(last_word.length() - 2));
    }
}

