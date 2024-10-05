        String longest_palindromic = longestPalindromic(string);
        String prefix = string.substring(0, string.length() - longest_palindromic.length());
        return string + new StringBuilder(prefix).reverse().toString();
    }
    /**
    Return the longest palindromic postfix of a supplied string.
     */
    private String longestPalindromic(String string) {
        int i = string.length();
        while (i > 0) {
            if (isPalindrome(string.substring(0, i))) {
                return string.substring(0, i);
            }
            i--;
        }
        return "";
    }
}

