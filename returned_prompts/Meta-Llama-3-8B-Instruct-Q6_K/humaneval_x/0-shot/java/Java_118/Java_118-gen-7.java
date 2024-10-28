    public String getClosestVowel(String word) {
        for (int i = word.length() - 3; i >= 0; i--) {
            if (!isVowel(word.charAt(i))) {
                for (int j = i + 1; j < word.length(); j++) {
                    if (isVowel(word.charAt(j))) {
                        return String.valueOf(word.charAt(j));
                    }
                }
            }
        }
        return "";
    }

    private boolean isVowel(char c) {
        return "AEIOUaeiou".indexOf(c) != -1;
    }
}

