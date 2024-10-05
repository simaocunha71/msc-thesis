        int sqrt_n = (int) Math.sqrt(n);
        for (int i = sqrt_n; i >= 2; i--) {
            if (n % i == 0) {
                return i;
            }
        }
        return -1;
    }
}
