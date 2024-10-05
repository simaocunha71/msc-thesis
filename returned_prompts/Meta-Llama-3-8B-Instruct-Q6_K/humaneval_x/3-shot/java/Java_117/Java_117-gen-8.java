        List<String> result = new ArrayList<>();
        String[] words = s.split(" ");
        for (String word : words) {
            int consonantCount = 0;
            for (char c : word.toLowerCase().toCharArray()) {
                if (!Character.isLetter(c)) continue;
                if (c != 'a' && c != 'e' && c != 'i' && c != 'o' && c != 'u') {
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

