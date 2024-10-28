        if (txt.isEmpty()) return false;

        String last_char = txt.substring(txt.length() - 1);
        String[] words = txt.split(" ");
        String last_word = words[words.length - 1];

        if (last_char.matches("[a-zA-Z]")) {
            if (last_word.equals(last_char)) {
                return true;
            }
        }
        return false;
    }
}

