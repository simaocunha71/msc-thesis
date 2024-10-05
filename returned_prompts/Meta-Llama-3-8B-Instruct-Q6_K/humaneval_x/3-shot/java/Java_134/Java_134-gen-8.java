        if (txt.length() == 0) return false;
        char last_char = txt.charAt(txt.length() - 1);
        return Character.isLetter(last_char) && !isPartOfWord(txt, last_char);
    }

    private boolean isPartOfWord(String txt, char c) {
        int i = txt.length() - 1;
        while (i > 0) {
            if (txt.charAt(i) == ' ') return true;
            i--;
        }
        return false;
    }
}
