        int even = 0, odd = 0;
        for (int i = 1; i <= n; i++) {
            if (isPalindrome(i)) {
                if (i % 2 == 0) even++;
                else odd++;
            }
        }
        return Arrays.asList(even, odd);

    }

    private boolean isPalindrome(int i) {
        String s = String.valueOf(i);
        for (int j = 0; j < s.length() / 2; j++) {
            if (s.charAt(j) != s.charAt(s.length() - 1 - j)) {
                return false;
            }
        }
        return true;
    }
}

