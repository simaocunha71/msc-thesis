        for (int i = word.length() - 1; i >= 0; i--) {
            char c = word.charAt(i);
            if (c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u' || c == 'A' || c == 'E' || c == 'I' || c == 'O' || c == 'U') {
                for (int j = i - 1; j >= 0; j--) {
                    char prev_c = word.charAt(j);
                    if (Character.isLetter(prev_c) && !isVowel(prev_c)) {
                        return String.valueOf(c);
                    }
                }
            }
        }
        return "";
    }

    private boolean isVowel(char c) {
        return c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u' || c == 'A' || c == 'E' || c == 'I' || c == 'O' || c == 'U';
    }
}

