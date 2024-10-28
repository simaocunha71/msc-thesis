        int even_count = 0;
        int odd_count = 0;
        for (int i = 1; i <= n; i++) {
            int j = reverse(i);
            if (i == j) {
                if (i % 2 == 0) {
                    even_count += 1;
                } else {
                    odd_count += 1;
                }
            }
        }
        return Arrays.asList(even_count, odd_count);
    }

    int reverse(int n) {
        int result = 0;
        int digit;
        while (n > 0) {
            digit = n % 10;
            result = result * 10 + digit;
            n /= 10;
        }
        return result;
    }
}

