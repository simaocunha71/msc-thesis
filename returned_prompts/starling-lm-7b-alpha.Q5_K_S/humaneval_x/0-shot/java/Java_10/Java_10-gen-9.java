        String res = "";
        StringBuilder sb = new StringBuilder(string);
        while (sb.length() > 0) {
            String sub = sb.substring(0, sb.length() / 2);
            if (isPalindrome(sub)) {
                res = sb.toString() + sub;
                break A;
            }
            sb.delete(0, sb.length() / 2);
        }
        return res;
    }

    /**
    Find the longest palindromic substring of given string
     */
    public String findLongestPalindrome(String string) {
        int n = string.length();
        boolean[][] table = new boolean[n][n];
        int maxLength = 1;
        int start = 0;
        for (int i = 0; i < n; i++) {
            table[i][i] = true;
        }
        for (int i = 0; i < n - 1; i++) {
            if (string.charAt(i) == string.charAt(i + 1)) {
                table[i][i + 1] = true;
                start = i;
                maxLength = 2;
            }
        }
        for (int k = 3; k <= n; k++) {
            for (int i = 0; i < n - k + 1; i++) {
                int j = i + k - 1;
                if (table[i + 1][j - 1] && string.charAt(i) == string.charAt(j)) {
                    table[i][j] = true;
                }
                if (table[i][j] && j - i + 1 > maxLength) {
                    start = i;
                    maxLength = j - i + 1;
                }
            }
        }

        return string.substring(start, start + maxLength);
    }
}










































