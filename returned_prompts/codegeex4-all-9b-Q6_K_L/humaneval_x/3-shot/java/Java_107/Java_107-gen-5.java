        int even_count = 0;
        int odd_count = 0;
        for (int i = 1; i <= n; i++) {
            if (isPalindrome(i)) {
                if (i % 2 == 0) {
                    even_count += 1;
                } else {
                    odd_count += 1;
                }
            }
        }
        return Arrays.asList(even_count, odd_count);
    }

    public boolean isPalindrome(int number) {
        String str = Integer.toString(number);
        return str.equals(new StringBuilder(str).reverse().toString());
    }
}

