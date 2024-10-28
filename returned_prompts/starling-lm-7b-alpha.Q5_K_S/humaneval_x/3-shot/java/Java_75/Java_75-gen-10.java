        int prime_factors_count = 0;
        int sqrt_a = (int) Math.sqrt(a);
        for (int i = 2; i <= sqrt_a; i++) {
            if (a % i == 0) {
                prime_factors_count += 1;
                while (a % i == 0) {
                    a /= i;
                }
            }
        }
        return prime_factors_count == 2 && a == 1;
    }
}

