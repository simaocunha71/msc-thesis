        List<Integer> list = new ArrayList<>();
        int even = 0, odd = 0;
        for (int i = 1; i <= n; i++) {
            if (isPalindrome(i)) {
                if (i % 2 == 0) {
                    even++;
                } else {
                    odd++;
                }
            }
        }
        list.add(even);
        list.add(odd);
        return list;
    }

    public boolean isPalindrome(int n) {
        int x = n, reverse = 0, remainder = 0;
        while (x > 0) {
            remainder = x % 10;
            reverse = reverse * 10 + remainder;
            x /= 10;
        }
        return (n == reverse);
    }
}































```