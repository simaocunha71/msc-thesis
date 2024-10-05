    // Pseudo code
    // Initialize result
    // Iterate through the string
    // Check if the letter is a vowel and is between two consonants
    // If so, save the result and break
    // If none found, return empty string

        StringBuilder res = new StringBuilder();
        char[] c = word.toCharArray();
        boolean found = false;
        for (int i = 1; i < c.length - 1; i++) {
            if (!isConsonant(c[i])) {
                if (found) {
                    break;
                }
                continue;
            }
            if (isVowel(c[i])) {
                res.append(c[i]);
                found = true;
                break;
            }
            if (isConsonant(c[i - 1]) && isConsonant(c[i + 1])) {
                res.append(c[i]);
                found = true;
                break;
            }
        }
        if (!found) {
            return "";
        }
        return res.toString();
    }

    private boolean isConsonant(char c) {
        return !isVowel(c) && c != ' ';
    }

    private boolean isVowel(char c) {
        return c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u';
    }

}


























































































































































