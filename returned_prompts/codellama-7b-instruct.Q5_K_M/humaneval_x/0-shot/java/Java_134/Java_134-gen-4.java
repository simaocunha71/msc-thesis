        // Your code here
        if (txt.length() == 0) return false;
        char last = txt.charAt(txt.length() - 1);
        if (!Character.isLetter(last)) return false;
        boolean foundSpace = false;
        for (int i = 0; i < txt.length(); i++) {
            char c = txt.charAt(i);
            if (c == ' ') {
                foundSpace = true;
            }
            if (!Character.isLetter(c)) {
                return false;
            }
        }
        return !foundSpace;
    }
}
