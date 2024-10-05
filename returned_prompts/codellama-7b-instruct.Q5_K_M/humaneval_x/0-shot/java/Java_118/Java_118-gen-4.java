        String vowel = "";
        for (int i = word.length()-1; i >= 0; i--) {
            if (isVowel(word.charAt(i))) {
                vowel = word.charAt(i)+"";
                break;
            }
            if (isConsonant(word.charAt(i))) {
                continue;
            }
            vowel = "";
            break;
        }
        return vowel;
    }

    public boolean isConsonant(char c) {
        if (c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u') {
            return false;
        }
        return true;
    }

    public boolean isVowel(char c) {
        if (c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u') {
            return true;
        }
        return false;
    }
}


