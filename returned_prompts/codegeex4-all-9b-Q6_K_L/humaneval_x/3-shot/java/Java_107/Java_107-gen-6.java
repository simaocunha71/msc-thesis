        int even_count = 0;
        int odd_count = 0;
        for (int i = 1; i <= n; i++) {
            String number_string = Integer.toString(i);
            String reversed_string = new StringBuilder(number_string).reverse().toString();
            if (number_string.equals(reversed_string)) {
                if (i % 2 == 0) even_count += 1;
                else odd_count += 1;
            }
        }
        return Arrays.asList(even_count, odd_count);
    }
}

