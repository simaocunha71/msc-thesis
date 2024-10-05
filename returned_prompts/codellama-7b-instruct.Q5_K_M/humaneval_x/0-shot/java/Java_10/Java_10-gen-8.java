        String prefix = "";
        String postfix = "";
        for (int i = 0; i < string.length(); i++) {
            String sub = string.substring(0, i+1);
            if (isPalindrome(sub)) {
                prefix = sub;
                break A;
            }
        }
        for (int i = string.length()-1; i >= 0; i--) {
            String sub = string.substring(i);
            if (isPalindrome(sub)) {
                postfix = sub;
                break A;
            }
        }
        return prefix + postfix;
    }
    /**
    Find the shortest string that can be obtained by removing some
    characters from supplied string in order to obtain a palindrome.
    >>> shortestPalindrome("racecar")
    "racecar"
    >>> shortestPalindrome("carrace")
    "racecar"
    >>> shortestPalindrome("carracec")
    "carracec"
     */
    public String shortestPalindrome(String string) {
        String palindrome = makePalindrome(string);
        return palindrome.substring(0, string.length());
    }
    public static void main(String[] args) {
        Solution s = new Solution();
        System.out.println(s.shortestPalindrome("racecar"));
    }
}
