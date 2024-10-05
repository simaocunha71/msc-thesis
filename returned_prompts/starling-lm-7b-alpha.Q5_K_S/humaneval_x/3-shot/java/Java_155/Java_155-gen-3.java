        int even_count = 0;
        int odd_count = 0;
        while (num > 0) {
            int d = num % 10;
            if (d % 2 == 0) {
                even_count += 1;
            } else {
                odd_count += 1;
            }
            num /= 10;
        }
        return Arrays.asList(even_count, odd_count);
    }
}

