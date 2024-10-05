        return powerModulo(2, n, p);
    }

    private int powerModulo(int a, int b, int mod) {
        int result = 1;
        a = a % mod; 
        while (b > 0)
        {
            if ((b & 1) == 1)
                result = (result * a) % mod;
            b = b >> 1; 
            a = (a * a) % mod;
        }
        return result;
    }
}

