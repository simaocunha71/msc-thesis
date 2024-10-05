        int result = 1;
        while (n > 0) {
            if (n % 2 == 1) {
                result = (result * (p % 2 == 0 ? 1 : p - 1)) % p;
            }
            n /= 2;
            p = (p * p) % p;
        }
        return result;
    }
}

