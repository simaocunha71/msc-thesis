        int even = 0;
        int odd = 0;
        for (int i = 1; i <= n; i++) {
            String s = String.valueOf(i);
            if (isPalindrome(s)) {
                if (isEven(i)) {
                    even++;
                } else {
                    odd++;
                }
            }
        }
        return Arrays.asList(even, odd);
    }

    private boolean isPalindrome(String s) {
        int left = 0, right = s.length() - 1;
        while (left < right) {
            if (s.charAt(left) != s.charAt(right)) {
                return false;
            }
            left++;
            right--;
        }
        return true;
    }

    private boolean isEven(int i) {
        return i % 2 == 0;
    }
}

