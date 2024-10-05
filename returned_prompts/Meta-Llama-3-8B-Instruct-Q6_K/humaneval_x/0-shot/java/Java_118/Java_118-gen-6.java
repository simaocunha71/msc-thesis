        int i = word.length() - 2;
        while (i >= 0 && !isVowel(word.charAt(i))) {
            i--;
        }
        if (i < 0) {
            return "";
        }
        int j = i - 1;
        while (j >= 0 && !isVowel(word.charAt(j))) {
            j--;
        }
        return word.substring(j + 1, i + 1);
    }

    private boolean isVowel(char c) {
        return "AEIOUaeiou".indexOf(c) != -1;
    }
}
