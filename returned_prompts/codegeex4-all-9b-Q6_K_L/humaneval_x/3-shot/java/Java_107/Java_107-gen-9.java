        int even = 0;
        int odd = 0;

        for (int i = 1; i <= n; i++) {
            String number = Integer.toString(i);
            if (number.equals(new StringBuilder(number).reverse().toString())) {
                if (i % 2 == 0) even += 1;
                else odd += 1;
            }
        }
        return Arrays.asList(even, odd);
    }
}

