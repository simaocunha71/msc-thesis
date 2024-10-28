        int i = 0;
        int j = string.length() - 1;
        while (i < j) {
            if (string.charAt(i)!= string.charAt(j)) {
                break;
            }
            i++;
            j--;
        }
        StringBuilder sb = new StringBuilder(string);
        sb.append(new StringBuilder(string).reverse());
        return sb.toString();
    }

    /**
    Find the shortest palindrome that begins with a supplied string.
    Algorithm idea is simple:
    - Find the longest postfix of supplied string that is a palindrome.
    - Append to the end of the string reverse of a string prefix that comes before the palindromic suffix.
    >>> makePalindrome("")
    ""
    >>> makePalindrome("cat")
    "catac"
    >>> makePalindrome("cata")
    "catac"
     */
    public String makePalindrome(String string) {

B:
        int i = 0;
        int j = string.length() - 1;
        while (i < j) {
            if (string.charAt(i)!= string.charAt(j)) {
                break;
            }
            i++;
            j--;
        }
        StringBuilder sb = new StringBuilder(string);
        sb.append(new StringBuilder(string).reverse());
        return sb.toString();
    }
}
