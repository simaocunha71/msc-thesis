public class Solution {
    /**
     * Test if given string is a palindrome
     */
    public boolean isPalindrome(String string) {
        int i = 0;
        int j = string.length() - 1;
        while (i < j) {
            if (string.charAt(i) != string.charAt(j)) {
                return false;
            }
            i++;
            j--;
        }
        return true;
    }

    /**
     * Find the shortest palindrome that begins with a supplied string.
     * Algorithm idea is simple:
     * - Find the longest postfix of supplied string that is a palindrome.
     * - Append to the end of the string reverse of a string prefix that comes before the palindromic suffix.
     * >>> makePalindrome("")
     * ""
     * >>> makePalindrome("cat")
     * "catac"
     * >>> makePalindrome("cata")
     * "catac"
     */
    public String makePalindrome(String string) {
        if (isPalindrome(string)) {
            return string;
        }
        for (int i = 0; i < string.length(); i++) {
            String postfix = string.substring(i);
            String prefix = string.substring(0, i);
            if (isPalindrome(postfix)) {
                String palindrome = string + new StringBuilder(prefix).reverse().toString();
                return palindrome;
            }
        }
        return null;
    }

    public static void main(String[] args) {
        Solution solution = new Solution();
        System.out.println(solution.makePalindrome(""));
        System.out.println(solution.makePalindrome("cat"));
        System.out.println(solution.makePalindrome("cata"));
    }
}