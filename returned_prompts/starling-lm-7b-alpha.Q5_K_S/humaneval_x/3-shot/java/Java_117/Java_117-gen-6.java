        List<String> result = new ArrayList<>();
        for (String w : s.split(" ")) {
            int count = 0;
            for (char c : w.toCharArray()) {
                if (!isVowel(c)) {
                    count += 1;
                }
                if (count == n) {
                    result.add(w);
                } else if (count > n) {
                    break;
                }
            }
        }
        return result;
    }

    private boolean isVowel(char c) {
        return c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u' || c == 'y';
    }
}

