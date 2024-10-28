public class Solution {
    /**
     * Checks if given string is a palindrome
     * >>> isPalindrome("")
     * true
     * >>> isPalindrome("aba")
     * true
     * >>> isPalindrome("aaaaa")
     * true
     * >>> isPalindrome("zbcd")
     * false
     */
    public boolean isPalindrome(String text) {
        if (text == null || text.length() == 0) {
            return true;
        }
        int left = 0;
        int right = text.length() - 1;
        while (left < right) {
            if (text.charAt(left) != text.charAt(right)) {
                return false;
            }
            left++;
            right--;
        }
        return true;
    }
}