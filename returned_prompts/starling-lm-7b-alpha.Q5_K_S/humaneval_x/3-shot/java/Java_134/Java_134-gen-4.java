        if (txt.length() == 0) return false;

        if (Character.isLetter(txt.charAt(txt.length() - 1))) {
            int pos = txt.length() - 1;
            while (pos >= 0 && Character.isWhitespace(txt.charAt(pos))) {
                pos--;
            }
            return pos == txt.length() - 1;
        }
        return false;
    }
}

