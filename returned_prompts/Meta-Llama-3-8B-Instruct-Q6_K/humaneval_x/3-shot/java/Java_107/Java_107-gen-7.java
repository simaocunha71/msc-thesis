        int even = 0, odd = 0;
        for (int i = 1; i <= n; i++) {
            String s = String.valueOf(i);
            if (s.equals(new StringBuilder(s).reverse().toString())) {
                if (i % 2 == 0) {
                    even++;
                } else {
                    odd++;
                }
            }
        }
        return Arrays.asList(even, odd);
    }
}

