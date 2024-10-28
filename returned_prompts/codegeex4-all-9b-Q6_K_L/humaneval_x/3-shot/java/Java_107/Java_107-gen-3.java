        int even = 0;
        int odd = 0;

        for (int i = 1; i <= n; i++) {
            if (isPalindrome(i)) {
                if (i % 2 == 0) {
                    even += 1;
                } else {
                    odd += 1;
                }
            }
        }
        return Arrays.asList(even, odd);
    }

    private boolean isPalindrome(int n) {
        String s = String.valueOf(n);
        for (int i = 0; i < s.length() / 2; i++) {
            if (s.charAt(i) != s.charAt(s.length() - i - 1)) {
                return false;
            }
        }
        return true;
    }
}

