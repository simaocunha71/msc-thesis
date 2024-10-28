        int even = 0;
        int odd = 0;
        for (int i = 1; i <= n; i++) {
            int number = i;
            while (number != 0) {
                int last_digit = number % 10;
                number /= 10;
                if (last_digit != 0) {
                    break;
                }
            }
            if (i % 2 == 0) {
                even += 1;
            } else {
                odd += 1;
            }
        }
        return new ArrayList<>(Arrays.asList(even, odd));
    }
}

```