        int result = 1;
        while (n > 0) {
            if (n % 2 == 1) result = (result * p) % p;
            p = (p * p) % p;
            n /= 2;
        }
        return result;
    }
}

