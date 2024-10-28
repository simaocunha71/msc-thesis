        int len = word.length();
        for (int i = len - 2; i >= 0; i--) {
            if (isVowel(word.charAt(i))) {
                for (int j = i + 1; j < len; j++) {
                    if (!isVowel(word.charAt(j))) {
                        return String.valueOf(word.charAt(i));
                    }
                }
            }
        }
        return "";
    }

    private boolean isVowel(char c) {
        return c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u';
    }
}

