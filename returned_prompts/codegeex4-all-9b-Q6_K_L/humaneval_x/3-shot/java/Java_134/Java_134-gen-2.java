        if (txt.isEmpty()) return false;
        char last_char = txt.charAt(txt.length() - 1);
        return Character.isLetter(last_char) && last_char != ' ';
    }
}

