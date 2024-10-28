        if (txt.length() == 0) return false;
        char last = txt.charAt(txt.length() - 1);
        return Character.isLetter(last) && !Character.isAlphabetic(last);
    }
}

