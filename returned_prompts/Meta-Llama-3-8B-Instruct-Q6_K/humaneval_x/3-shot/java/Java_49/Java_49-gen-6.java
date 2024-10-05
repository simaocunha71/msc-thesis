        return (int) ((Math.pow(2, n)) % p);
    }
} // This solution is not correct. It's not safe to use pow() function as it can lead to overflow for large values of n and p.

