        List<String> result = new ArrayList<>();
        String[] words = s.split("\\s+");
        for (String word : words) {
            int consonant_count = 0;
            for (char c : word.toCharArray()) {
                if (c != 'a' && c != 'e' && c != 'i' && c != 'o' && c != 'u' && c != ' ') {
                    consonant_count++;
                }
            }
            if (consonant_count == n) {
                result.add(word);
            }
        }
        return result;
    }
}

