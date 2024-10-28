        int even = 0, odd = 0;
        for (int i = 1; i <= n; i++) {
            if (isPalindrome(i) && i % 2 == 0) even++;
            if (isPalindrome(i) && i % 2 != 0) odd++;
        }
        return Arrays.asList(even, odd);
    }

    private boolean isPalindrome(int num) {
        int reversed = 0;
        int original = num;
        while (num > 0) {
            int digit = num % 10;
            reversed = reversed * 10 + digit;
            num /= 10;
        }
        return original == reversed;
    }
}

