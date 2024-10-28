        int result = 1;

        for (int i = 2; i <= n; i++) {
            while (n % i == 0) {
                result = i;
                n /= i;
            }
        }
        return result;
    }
}

