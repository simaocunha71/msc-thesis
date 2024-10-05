        if (n == 0) return 1;
        if (n % 2 == 0) {
            return modp((n / 2) % p, p) * modp((n / 2) % p, p) % p;
        } else {
            return n * modp((n - 1) / p, p) % p;
        }
    }
}

