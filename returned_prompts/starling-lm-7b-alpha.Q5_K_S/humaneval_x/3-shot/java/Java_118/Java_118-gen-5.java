        String vowel = "";
        for (int i = 0; i < word.length(); i++) {
            if (isVowel(word.charAt(i))) {
                char right = word.charAt(i + 1);
                char left = word.charAt(i - 1);
                if (right == ' ' || right == '$') {
                    vowel = String.valueOf(word.charAt(i));
                    break;
                } else if (left == ' ' || left == '$') {
                    vowel = String.valueOf(word.charAt(i));
                    break;
                }
            }
        }
        return vowel;
    }

    private boolean isVowel(char c) {
        return "aeiou".indexOf(c) >= 0;
    }
}

