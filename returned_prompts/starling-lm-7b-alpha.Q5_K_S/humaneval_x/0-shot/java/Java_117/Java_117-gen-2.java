    List<String> res = new ArrayList<>();
    boolean[] vowel = new boolean[26];
    boolean[] consonant = new boolean[26];
    for(int i = 0; i < 26; i++) {
        vowel[i] = (s.charAt(i) == 'a' || s.charAt(i) == 'e' || s.charAt(i) == 'i' ||
        s.charAt(i) == 'o' || s.charAt(i) == 'u' || s.charAt(i) == 'y');
        consonant[i] = !vowel[i];
    }

    // Iterate over each word in the string
    StringBuilder sb = new StringBuilder();
    for(char c: s.toCharArray()) {
        if(c == ' ') {
            // If a word is formed
            if(sb.length() != 0) {
                // Check if the formed word has exactly n consonants
                if(countConsonants(sb.toString(), consonant) == n) {
                    res.add(sb.toString());
                }
                // Reset the StringBuilder
                sb = new StringBuilder();
            }
        } else {
            sb.append(c);
        }
    }
    if(sb.length() != 0) {
        // If the last word has exactly n consonants, add it to the result
        if(countConsonants(sb.toString(), consonant) == n) {
            res.add(sb.toString());
        }
    }
    return res;
}

private int countConsonants(String word, boolean[] consonant) {
    int count = 0;
    for(char c: word.toCharArray()) {
        if(!consonant[c - 'a']) {
            count++;
        }
    }
    return count;
}

}
















































