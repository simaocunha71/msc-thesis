        if (txt.length() == 0) return false;

        for (int i = txt.length() - 1; i >= 0; i--) {
            if (Character.isAlphabetic(txt.charAt(i))) {
                if (i == 0 || txt.charAt(i - 1) == ' ') return true;
            }
        }
        return false;
    }
}

