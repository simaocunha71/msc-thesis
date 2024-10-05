        int even = 0;
        int odd = 0;
        while (num != 0) {
            if (num % 2 == 0) {
                even += 1;
            } else {
                odd += 1;
            }
            num /= 10;
        }
        return Arrays.asList(even, odd);
    }
}

