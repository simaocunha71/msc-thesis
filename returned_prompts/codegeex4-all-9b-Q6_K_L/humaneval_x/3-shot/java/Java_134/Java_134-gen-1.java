        if (txt.length() == 0) return false;
        char last_char = txt.charAt(txt.length() - 1);
        return Character.isLetter(last_char) && (txt.lastIndexOf(last_char) == txt.length() - 1);
    }
}

