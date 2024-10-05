        return powerMod(2, n, p);
    }

    private int powerMod(int base, int exponent, int modulo) {
        int result = 1;
        base = base % modulo;
        while (exponent > 0) {
            if ((exponent & 1) == 1)
                result = (result * base) % modulo;
            exponent = exponent >> 1;
            base = (base * base) % modulo;
        }
        return result;
    }
}

