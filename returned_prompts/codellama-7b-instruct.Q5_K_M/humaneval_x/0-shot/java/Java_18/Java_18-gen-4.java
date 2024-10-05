        if (string == null || substring == null) {
            return 0;
        }

        if (string.length() < substring.length()) {
            return 0;
        }

        int count = 0;
        for (int i = 0; i < string.length() - substring.length() + 1; i++) {
            String current = string.substring(i, i + substring.length());
            if (current.equals(substring)) {
                count++;
            }
        }
        return count;
    }

    /**
    Given a string, find the longest palindrome in it.
    >>> longestPalindrome("racecar")
    "racecar"
    >>> longestPalindrome("level")
    "level"
    >>> longestPalindrome("test")
    "t"
    >>> longestPalindrome("abcdcba")
    "abcdcba"
     */
    public String longestPalindrome(String s) {
        // TODO
        return "";
    }

    public static void main(String[] args) {
        Solution solution = new Solution();
        System.out.println(solution.howManyTimes("", "a"));
        System.out.println(solution.howManyTimes("aaa", "a"));
        System.out.println(solution.howManyTimes("aaaa", "aa"));
        System.out.println(solution.longestPalindrome("racecar"));
        System.out.println(solution.longestPalindrome("level"));
        System.out.println(solution.longestPalindrome("test"));
        System.out.println(solution.longestPalindrome("abcdcba"));
    }
}
