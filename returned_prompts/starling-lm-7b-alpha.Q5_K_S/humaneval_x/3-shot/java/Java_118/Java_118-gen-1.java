        boolean isVowel = (c -> "aeiou".contains(c.toString().toLowerCase()));

        int first_consonant_index = word.length();
        int second_consonant_index = -1;
        for (int i = word.length() - 1; i >= 0; i--) {
            if (isVowel.test(word.charAt(i))) {
                continue;
            }
            if (first_consonant_index == word.length()) {
                first_consonant_index = i;
            } else {
                second_consonant_index = i;
            }
        }
        if (second_consonant_index == -1) {
            return "";
        }
        if (first_consonant_index + 1 < second_consonant_index) {
            return String.valueOf(word.charAt(first_consonant_index + 1));
        } else {
            return String.valueOf(word.charAt(second_consonant_index - 1));
        }
    }
}

