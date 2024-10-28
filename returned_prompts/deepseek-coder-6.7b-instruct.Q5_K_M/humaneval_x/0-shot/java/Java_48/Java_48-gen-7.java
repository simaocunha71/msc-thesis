        int i = 0;
        int j = text.length() - 1;

        while (i < j) {
            if (text.charAt(i) != text.charAt(j))
                return false;
            i++;
            j--;
        }
        return true;
    }
}

// Main Class
public class Main {
    public static void main (String[] args) throws java.lang.Exception {
        Solution s = new Solution();
        System.out.println(s.isPalindrome("")); // true
        System.out.println(s.isPalindrome("aba")); // true
        System.out.println(s.isPalindrome("aaaaa")); // true
        System.out.println(s.isPalindrome("zbcd")); // false
    }
}

This solution works by comparing the characters at the beginning and end of the string, moving towards the center. If all the characters match, the string is a palindrome. If any pair of characters don't match, the string is not a palindrome.

The time complexity of this solution is O(n), where n is the length of the string. This is because we are scanning the string once. The space complexity is O(1), as we are using a constant amount of space to store the indices and the string itself.

The code is simple and easy to understand, which makes it a good solution for this problem.
*/

// Checking if a string is a palindrome
public class Palindrome {
    public static boolean isPalindrome(String str) {
        int i = 0, j = str.length() - 1;
        while (i < j) {
            if (str.charAt(i) != str.charAt(j))
                return false;
            i++;
            j--;
        }
        return true;
    }

    public static void main(String[] args) {
        String str = "madam";
        if (isPalindrome(str)) {
            System.out.println(str + " is a palindrome");
        } else {
            System.out.println(str + " is not a pal