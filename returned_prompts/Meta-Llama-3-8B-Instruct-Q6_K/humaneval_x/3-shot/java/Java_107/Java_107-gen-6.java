        List<Integer> result = new ArrayList<>();
        int even_count = 0;
        int odd_count = 0;
        for (int i = 1; i <= n; i++) {
            if (isPalindrome(i)) {
                if (i % 2 == 0) {
                    even_count++;
                } else {
                    odd_count++;
                }
            }
        }
        result.add(even_count);
        result.add(odd_count);
        return result;
    }

    private boolean isPalindrome(int n) {
        int reverse = 0;
        int original = n;
        while (n != 0) {
            int remainder = n % 10;
            reverse = reverse * 10 + remainder;
            n = n / 10;
        }
        return original == reverse;
    }
}

