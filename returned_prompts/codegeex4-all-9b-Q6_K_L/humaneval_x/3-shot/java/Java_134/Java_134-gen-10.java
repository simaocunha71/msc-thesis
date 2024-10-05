        if (txt.length() == 0) {
            return false;
        }

        char last_char = txt.charAt(txt.length() - 1);

        if (!Character.isLetter(last_char)) {
            return false;
        }

        if (txt.charAt(txt.length() - 2) == ' ') {
            return false;
        }

        return true;
    }
}

