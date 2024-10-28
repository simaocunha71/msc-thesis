        int even = 0;
        int odd = 0;

        for (int i = 1; i <= n; i++) {
            String str = Integer.toString(i);
            if (str.equals(new StringBuilder(str).reverse().toString())) {
                if (i % 2 == 0) {
                    even += 1;
                } else {
                    odd += 1;
                }
            }
        }
        return Arrays.asList(even, odd);
    }
}

