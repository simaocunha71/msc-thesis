        List<String> result = new ArrayList<>();
        String[] words = s.split("\\s+");

        for (String word : words) {
            int consonantCount = 0;
            for (char c : word.toLowerCase().toCharArray()) {
                if (c != 'a' && c != 'e' && c != 'i' && c != 'o' && c != 'u' && c != ' ') {
                    consonantCount++;
                }
            }
            if (consonantCount == n) {
                result.add(word);
            }
        }
        return result;
    }
}