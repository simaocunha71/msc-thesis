        for (int i = word.length() - 1; i >= 0; i--) {
            char ch = word.charAt(i);
            if (ch == 'a' || ch == 'e' || ch == 'i' || ch == 'o' || ch == 'u' || ch == 'A' || ch == 'E' || ch == 'I' || ch == 'O' || ch == 'U') {
                if (isConsonant(word, i)) {
                    return String.valueOf(ch);
                }
            }
        }
        return "";
    }

    private boolean isConsonant(String word, int i) {
        if (i == 0) {
            return true;
        }
        return !("aeiouAEIOU".indexOf(word.charAt(i - 1)) != -1);
    }
}

