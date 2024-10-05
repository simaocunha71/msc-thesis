public class Solution {
    public String getClosestVowel(String word) {
        StringBuilder sb = new StringBuilder();
        for (int i = word.length() - 1; i >= 0; i--) {
            char ch = word.charAt(i);
            if (isVowel(ch)) {
                if (sb.length() == 0 || !isConsonant(word.charAt(i - 1))) {
                    return String.valueOf(ch);
                }
                sb.append(ch);
            }
        }
        return "";
    }

    private boolean isVowel(char ch) {
        return ch == 'a' || ch == 'e' || ch == 'i' || ch == 'o' || ch == 'u' ||
               ch == 'A' || ch == 'E' || ch == 'I' || ch == 'O' || ch == 'U';
    }

    private boolean isConsonant(char ch) {
        return !isVowel(ch) && (ch >= 'a' && ch <= 'z' || ch >= 'A' && ch <= 'Z');
    }
}