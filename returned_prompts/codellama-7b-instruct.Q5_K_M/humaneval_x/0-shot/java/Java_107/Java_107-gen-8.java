        int even = 0;
        int odd = 0;
        for (int i = 1; i < n; i++) {
            if (isPalindrome(i)) {
                if (isEven(i)) {
                    even++;
                } else {
                    odd++;
                }
            }
        }
        return Arrays.asList(even, odd);
    }

    private boolean isPalindrome(int n) {
        String str = String.valueOf(n);
        if (str.equals(str.substring(0, str.length() / 2))) {
            return true;
        } else {
            return false;
        }
    }

    private boolean isEven(int n) {
        if (n % 2 == 0) {
            return true;
        } else {
            return false;
        }
    }
}

