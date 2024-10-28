        String result = "";

        for (int i = 0; i < text.length(); i++) {
            char ch = text.charAt(i);
            if (ch != 'a' && ch != 'e' && ch != 'i' && ch != 'o' && ch != 'u'
                    && ch != 'A' && ch != 'E' && ch != 'I' && ch != 'O' && ch != 'U') {
                result += ch;
            }
        }

        return result;
    }

    public static void main(String[] args) {
        Solution solution = new Solution();

        System.out.println(solution.removeVowels(""));
        System.out.println(solution.removeVowels("abcdef\nghijklm"));
        System.out.println(solution.removeVowels("abcdef"));
        System.out.println(solution.removeVowels("aaaaa"));
        System.out.println(solution.removeVowels("aaBAA"));
        System.out.println(solution.removeVowels("zbcd"));
    }
}

I:
import java.util.*;
import java.lang.*;

class Solution  {
    public String removeVowels(String text)  {
        String result = "";

        for (int i = 0; i < text.length(); i++) {
            char ch = text.charAt(i);
            if (ch != 'a' && ch != 'e' && ch != 'i' && ch != 'o' && ch != 'u'
                    && ch != 'A' && ch != 'E' && ch != 'I' && ch != 'O' && ch != 'U') {
                result += ch;
            }
        }

        return result;
    }

    public static void main(String[] args) {
        Solution solution = new Solution();

        System.out.println(solution.removeVowels(""));
        System.out.println(solution.removeVowels("