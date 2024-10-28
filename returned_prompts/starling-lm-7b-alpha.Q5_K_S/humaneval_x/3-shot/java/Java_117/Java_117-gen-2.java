        List<String> result = new ArrayList<>();
        boolean[] consonants = new boolean[26];
        for (char c : "aeiou".toCharArray()) {
            consonants[c - 'a'] = false;
        }
        for (char c : "bcdfghjklmnpqrstvwxyz".toCharArray()) {
            consonants[c - 'a'] = true;
        }

        for (String word : s.split(" ")) {
            int consonant_count = 0;
            for (char c : word.toCharArray()) {
                if (consonants[c - 'a']) {
                    consonant_count += 1;
                }
                if (consonant_count > n) {
                    break;
                }
            }
            if (consonant_count == n) {
                result.add(word);
            }
        }
        return result;
    }
}

