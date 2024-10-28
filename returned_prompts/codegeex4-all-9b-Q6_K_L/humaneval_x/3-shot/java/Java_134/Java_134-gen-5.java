        if (txt.length() == 0) {
            return false;
        }

        char last_char = txt.charAt(txt.length() - 1);
        return Character.isLetter(last_char) && !Character.isAlphabetic(last_char);
    }
}

