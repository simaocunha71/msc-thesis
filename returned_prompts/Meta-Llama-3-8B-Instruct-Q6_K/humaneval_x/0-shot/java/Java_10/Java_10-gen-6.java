    import java.util.*;

    public class Solution {
        public String makePalindrome(String s) {
            if (s == null || s.length() == 0) {
                return "";
            }
            int i = 0;
            int j = s.length() - 1;
            while (i < j) {
                if (s.charAt(i) != s.charAt(j)) {
                    break;
                }
                i++;
                j--;
            }
            String palindrome = s.substring(i, j + 1);
            String reverse = s.substring(0, i);
            String result = reverse + palindrome + new StringBuilder(palindrome).reverse().toString();
            return result;
        }
    }

