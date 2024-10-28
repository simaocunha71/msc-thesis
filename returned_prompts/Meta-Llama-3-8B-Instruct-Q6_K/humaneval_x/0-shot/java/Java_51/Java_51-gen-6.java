public class Solution {
    public String removeVowels(String text) {
        String result = "";
        for (char c : text.toCharArray()) {
            if (!isVowel(c)) {
                result += c;
            }
        }
        return result;
    }

    private boolean isVowel(char c) {
        c = Character.toLowerCase(c);
        return c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u';
    }
}A
A
