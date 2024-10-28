        if (txt.length() == 0) return false;

        int last_index = txt.length() - 1;
        if (txt.charAt(last_index) != ' ') return false;
        return Character.isLetter(txt.charAt(last_index - 1));
    }
}

