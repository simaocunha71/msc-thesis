        int evenCount = 0, oddCount = 0;
        for (int i = 1; i <= n; i++) {
            if (isPalindrome(i)) {
                if (i % 2 == 0) {
                    evenCount++;
                } else {
                    oddCount++;
                }
            }
        }
        return Arrays.asList(evenCount, oddCount);
    }

    private boolean isPalindrome(int num) {
        int reverse = 0, original = num;
        while (num != 0) {
            reverse = reverse * 10 + num % 10;
            num = num / 10;
        }
        return original == reverse;
    }
}

