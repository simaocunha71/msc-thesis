        List<String> result = new ArrayList<>();
        boolean[] consonant = new boolean[26];
        Arrays.fill(consonant, true);
        consonant['A'] = consonant['E'] = consonant['I'] = consonant['O'] = consonant['U'] = consonant['Y'] = false;

        for (int i = 0; i < s.length(); i++) {
            if (consonant[s.charAt(i) - 'a']) {
                n--;
            }
            if (n == 0) {
                String word = "";
                for (int j = i; j < s.length(); j++) {
                    word += s.charAt(j);
                    if (consonant[s.charAt(j) - 'a']) {
                        n--;
                    }
                    if (n == 0) {
                        result.add(word);
                        n = consonant[s.charAt(j) - 'a'] ? 1 : 0;
                    }
                }
                n = consonant[s.charAt(i) - 'a'] ? 1 : 0;
            }
        }
        return result;
    }
}


```