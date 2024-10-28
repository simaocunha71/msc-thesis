        if (txt.length() == 0) {
            return false;
        }
        char last_char = txt.charAt(txt.length() - 1);
        if (!Character.isLetter(last_char)) {
            return false;
        }
        return txt.lastIndexOf(last_char) == txt.length() - 1;
    }
}

