        if (txt.length() == 0) {
            return false;
        }
        if (txt.charAt(txt.length() - 1) >= 'a' && txt.charAt(txt.length() - 1) <= 'z' ||
                txt.charAt(txt.length() - 1) >= 'A' && txt.charAt(txt.length() - 1) <= 'Z') {
            return !Character.isLetter(txt.charAt(txt.length() - 2)) ||
                    txt.charAt(txt.length() - 2) == ' ';
        }
        return false;
    }
}

