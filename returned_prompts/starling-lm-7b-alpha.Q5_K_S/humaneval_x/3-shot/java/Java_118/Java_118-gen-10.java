        String vowel = "";
        List<Character> consonants = new ArrayList<>();
        for (char c : word.toCharArray()) {
            if (isConsonant(c)) {
                consonants.add(c);
            }
        }
        if (consonants.size() < 2) return vowel;
        for (int i = 0; i < consonants.size() - 1; i++) {
            if (vowel.isEmpty() && isVowel(consonants.get(i))) {
                vowel = String.valueOf(consonants.get(i));
            } else if (!vowel.isEmpty() && isVowel(consonants.get(i)) && isConsonant(consonants.get(i + 1))) {
                vowel = String.valueOf(consonants.get(i));
            } else if (!vowel.isEmpty() && isConsonant(consonants.get(i)) && isVowel(consonants.get(i + 1))) {
                vowel = String.valueOf(consonants.get(i + 1));
            }
        }
        return vowel;
    }

    public boolean isConsonant(char c) {
        return !isVowel(c);
    }

    public boolean isVowel(char c) {
        return "aeiou".contains(String.valueOf(c).toLowerCase());
    }
}

