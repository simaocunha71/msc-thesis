        int prime_count = 0;

        for (int i = 2; i < a; i++) {
            if (a % i == 0) {
                prime_count += 1;
                if (prime_count > 2) {
                    return false;
                }
            }
        }
        return prime_count == 2;
    }
}

