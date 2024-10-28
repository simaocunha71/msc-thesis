        List<String> result = new ArrayList<>();

        for (String word : s.split(" ")) {
            int consonants = 0;
            for (char c : word.toCharArray()) {
                if (c != 'a' && c != 'e' && c != 'i' && c != 'o' && c != 'u') {
                    consonants += 1;
                }
            }
            if (consonants == n) {
                result.add(word);
            }
        }
        return result;
    }
}

