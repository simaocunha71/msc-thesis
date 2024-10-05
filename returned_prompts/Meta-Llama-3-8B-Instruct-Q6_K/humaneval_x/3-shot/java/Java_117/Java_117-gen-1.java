        List<String> result = new ArrayList<>();
        String[] words = s.split(" ");
        for (String word : words) {
            int consonantCount = 0;
            for (char c : word.toCharArray()) {
                if (!Character.isLetter(c) || Character.isLetter(c) && !isVowel(c)) {
                    consonantCount++;
                }
            }
            if (consonantCount == n) {
                result.add(word);
            }
        }
        return result;
    }

    public boolean isVowel(char c) {
        c = Character.toLowerCase(c);
        return c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u';
    }
}

