    public String getClosestVowel(String word) {
        StringBuilder sb = new StringBuilder();
        for (int i = word.length() - 1; i > 0; i--) {
            char ch = word.charAt(i);
            if (ch == 'a' || ch == 'e' || ch == 'i' || ch == 'o' || ch == 'u' || ch == 'A' || ch == 'E' || ch == 'I' || ch == 'O' || ch == 'U') {
                sb.append(ch);
                return sb.toString();
            }
        }
        return "";
    }
}

Explanation:
This solution iterates through the word from right to left. It checks each character to see if it's a vowel. If it is, it appends it to a string builder and returns the string. If it doesn't find a vowel after checking each character, it returns an empty string. This way, it always returns the closest vowel that stands between two consonants from the right side of the word.