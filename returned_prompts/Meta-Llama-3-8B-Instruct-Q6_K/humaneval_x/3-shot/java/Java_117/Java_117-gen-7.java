        List<String> result = new ArrayList<>();
        String[] words = s.split("\\s+");

        for (String word : words) {
            int consonants = 0;
            for (char c : word.toCharArray()) {
                if (!Character.isLetter(c) || c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u') {
                    continue;
                }
                consonants++;
            }
            if (consonants == n) {
                result.add(word);
            }
        }
        return result;
    }
}

