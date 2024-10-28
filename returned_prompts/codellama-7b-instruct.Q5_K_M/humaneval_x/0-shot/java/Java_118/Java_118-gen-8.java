        for (int i = word.length() - 1; i >= 0; i--) {
            char ch = word.charAt(i);
            if (isVowel(ch)) {
                return String.valueOf(ch);
            }
            if (isConsonant(ch)) {
                continue;
            }
            return "";
        }
        return "";
    }

    private boolean isConsonant(char ch) {
        if (ch == 'q' || ch == 'w' || ch == 'r' || ch == 't' || ch == 'p' || ch == 's' || ch == 'd' || ch == 'f' || ch == 'g'
                || ch == 'h' || ch == 'j' || ch == 'k' || ch == 'l' || ch == 'z' || ch == 'x' || ch == 'c' || ch == 'v' || ch == 'b'
                || ch == 'n' || ch == 'm') {
            return true;
        }
        return false;
    }

    private boolean isVowel(char ch) {
        if (ch == 'a' || ch == 'e' || ch == 'i' || ch == 'o' || ch == 'u' || ch == 'y') {
            return true;
        }
        return false;
    }
}

