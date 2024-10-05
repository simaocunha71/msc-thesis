        List<String> result = new ArrayList<>();
        String[] words = s.split("\\s+");

        for (String word : words) {
            int consonantCount = 0;
            for (char c : word.toLowerCase().toCharArray()) {
                if (!isVowel(c)) {
                    consonantCount++;
                }
            }
            if (consonantCount == n) {
                result.add(word);
            }
        }
        return result;

    }

    private boolean isVowel(char c) {
        return "aeiou".indexOf(c) != -1;
    }
}

