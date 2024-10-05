    int i = 0;
    int j = text.size() - 1;
    while (i < j){
        if (text[i] != text[j])
            return false;
        i++;
        j--;
    }
    return true;
}

int main(){
    printf("%s\n", is_palindrome("") ? "true" : "false");
    printf("%s\n", is_palindrome("aba") ? "true" : "false");
    printf("%s\n", is_palindrome("aaaaa") ? "true" : "false");
    printf("%s\n", is_palindrome("zbcd") ? "true" : "false");
    return 0;
}

*/

//src/main/java/com/tel_ran/shkoda/palindrome/PalindromeChecker.java
package com.tel_ran.shkoda.palindrome;

public class PalindromeChecker {

    public static void main(String[] args) {
        System.out.println(isPalindrome(""));
        System.out.println(isPalindrome("aba"));
        System.out.println(isPalindrome("aaaaa"));
        System.out.println(isPalindrome("zbcd"));
    }

    public static boolean isPalindrome(String text) {
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

//src/main/java/com/tel_ran/shkoda/palindrome/PalindromeChecker2.java
package com.tel_ran.shkoda.palindrome;

public class PalindromeChecker2 {

    public static void main(String[] args) {
        System.out.println(isPalindrome(""));
        System.out.println(isPalindrome("aba"));
       