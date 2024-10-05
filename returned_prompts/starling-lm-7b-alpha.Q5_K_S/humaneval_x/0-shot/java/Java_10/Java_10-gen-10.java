        String reverse = "";
        String result = "";
        for (int i = string.length() - 1; i >= 0; i--) {
            reverse += string.charAt(i);
        }
        String palindrome = "";
        for (int i = string.length(); i >= 0; i--) {
            String substring = string.substring(0, i);
            String rev = reverse(substring);
            String concat = substring + palindrome + rev;
            if (isPalindrome(concat)) {
                palindrome = concat;
                result = palindrome + reverse;
                break A;
            }
        }
        return result;
    }
    /**
    Get the reverse of a given string.
    >>> reverse("")
    ""
    >>> reverse("abc")
    "cba"
    >>> reverse("cata")
    "atac"
     */
    public String reverse(String string) {
        char[] chars = string.toCharArray();
        int i = 0;
        int j = string.length() - 1;
        while (i < j) {
            char temp = chars[i];
            chars[i] = chars[j];
            chars[j] = temp;
            i++;
            j--;
        }
        return String.valueOf(chars);
    }
}



























```