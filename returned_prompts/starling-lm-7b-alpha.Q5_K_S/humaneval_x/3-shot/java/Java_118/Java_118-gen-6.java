        boolean vowel = c -> c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u';
        for (int i = 0; i < word.length() - 1; i++) {
            if (!vowel.test(word.charAt(i)) && !vowel.test(word.charAt(i + 1))) {
                for (char c = 'a'; c <= 'z'; c++) {
                    if (vowel.test(c)) {
                        int distance = i + 1;
                        if (distance > word.length() - i - 1) {
                            distance = word.length() - i - 1;
                        }
                        if (distance < 1) {
                            continue;
                        }
                        if (distance == 1 && word.charAt(i + 1) != c) {
                            continue;
                        }
                        return String.valueOf(c);
                    }
                }
            }
        }
        return "";
    }
}

