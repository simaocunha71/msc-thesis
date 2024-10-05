        for (int i = 2; i <= Math.sqrt(n); i++) {
            if (n % i == 0) {
                n /= i;
                i -= 1;
            }
        }
        return n;
    }
}

