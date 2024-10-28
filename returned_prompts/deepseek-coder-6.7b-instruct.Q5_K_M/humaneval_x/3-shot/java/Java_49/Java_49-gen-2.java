        return powerMod(2, n, p);
     }

     private int powerMod(int base, int exponent, int modulus) {
        int result = 1;
        while (exponent > 0) {
            if ((exponent & 1) == 1) {
                result = (result * base) % modulus;
            }
            exponent = exponent >> 1;
            base = (base * base) % modulus;
        }
        return result;
    }
}

