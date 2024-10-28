        int i = n % p;
        if (i < 0) i += p;
        return i;
    }

    /**
    Return 2^n modulo p (be aware of numerics).