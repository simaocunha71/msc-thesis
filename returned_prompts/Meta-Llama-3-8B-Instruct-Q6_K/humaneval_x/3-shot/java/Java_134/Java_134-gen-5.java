        if (txt.length() == 0) {
            return false;
        }
        char lastChar = txt.charAt(txt.length() - 1);
        if (!Character.isLetter(lastChar)) {
            return false;
        }
        for (int i = txt.length() - 2; i >= 0; i--) {
            if (Character.isLetter(txt.charAt(i))) {
                return true;
            }
        }
        return false;
    }
}

