        int last_consonant_index = -1;
        int first_consonant_index = -1;
        boolean last_char_is_vowel = false;
        boolean first_char_is_vowel = false;

        for (int i = 0; i < word.length(); i++) {
            if (isVowel(word.charAt(i))) {
                if (last_char_is_vowel) {
                    first_consonant_index = i;
                } else {
                    last_consonant_index = i;
                    last_char_is_vowel = true;
                }
            } else {
                if (first_char_is_vowel) {
                    last_consonant_index = i;
                } else {
                    first_consonant_index = i;
                    first_char_is_vowel = true;
                }
            }
        }

        if (last_consonant_index == -1 || first_consonant_index == -1) {
            return "";
        }
        return "" + word.charAt(last_consonant_index + 1);
    }

    private boolean isVowel(char c) {
        return c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u';
    }
}

