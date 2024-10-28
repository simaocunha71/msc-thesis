        int index = -1;
        for (int i = word.length() - 1; i >= 0; i--) {
            if (isVowel(word.charAt(i))) {
                index = i;
                break;
            }
        }
        if (index == -1) return "";
        for (int i = index - 1; i >= 0; i--) {
            if (!isVowel(word.charAt(i))) {
                return String.valueOf(word.charAt(i));
            }
        }
        return "";
    }

    private boolean isVowel(char c) {
        return "AEIOUaeiou".indexOf(c) != -1;
    }
}

