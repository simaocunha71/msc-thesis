public class Palindrome {
    public static boolean isPalindrome(String string) {
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

    public static void main(String[] args) {
        String string = "cat";
        System.out.println(isPalindrome(string));
        string = "catac";
        System.out.println(isPalindrome(string));
        string = "cata";
        System.out.println(isPalindrome(string));
    }
}

