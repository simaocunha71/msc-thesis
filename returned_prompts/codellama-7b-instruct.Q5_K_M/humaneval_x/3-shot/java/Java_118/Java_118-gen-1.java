        for (int i = word.length() - 1; i >= 0; i--) {
            if (isVowel(word.charAt(i))) {
                if (!isVowel(word.charAt(i + 1))) {
                    return String.valueOf(word.charAt(i));
                }
            }
            if (!isConsonant(word.charAt(i))) {
                continue;
            }
        }
        return "";
    }

    private boolean isVowel(char c) {
        return c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u';
    }

    private boolean isConsonant(char c) {
        return !isVowel(c);
    }
}

