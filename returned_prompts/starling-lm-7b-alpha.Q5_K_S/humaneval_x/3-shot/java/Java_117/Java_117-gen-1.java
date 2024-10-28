        List<String> result = new ArrayList<>();
        for (String word : s.split(" ")) {
            int consonants = 0;
            for (int i = 0; i < word.length(); i++) {
                char c = word.charAt(i);
                if (c != 'a' && c != 'e' && c != 'i' && c != 'o' && c != 'u' && c != ' ' && c != '.') {
                    consonants += 1;
                    if (consonants > n) {
                        break;
                    }
                }
            }
            if (consonants == n) {
                result.add(word);
            }
        }
        return result;
    }
}

