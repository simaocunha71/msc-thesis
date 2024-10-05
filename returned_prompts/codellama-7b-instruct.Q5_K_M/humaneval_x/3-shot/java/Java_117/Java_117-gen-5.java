        List<String> result = new ArrayList<>();

        if (n <= 0) return result;

        String[] words = s.split(" ");

        for (String word : words) {
            int consonants = 0;
            for (int i = 0; i < word.length(); i++) {
                char c = word.charAt(i);
                if (c != 'a' && c != 'e' && c != 'i' && c != 'o' && c != 'u') {
                    consonants++;
                }
            }

            if (consonants == n) {
                result.add(word);
            }
        }
        return result;
    }
}

