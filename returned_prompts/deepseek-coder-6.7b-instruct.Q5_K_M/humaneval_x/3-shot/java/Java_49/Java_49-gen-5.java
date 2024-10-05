        return power(2, n, p);

    }

    private int power(int base, int exponent, int modulus) {
        int c = 1;
        while (exponent > 0) {
            if ((exponent & 1) == 1) {
                c = (c * base) % modulus;
            }
            exponent >>= 1;
            base = (base * base) % modulus;
        }
        return c;
    }
}

