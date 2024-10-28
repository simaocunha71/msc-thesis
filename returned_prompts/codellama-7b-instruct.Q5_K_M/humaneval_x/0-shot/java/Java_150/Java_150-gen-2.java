        if (n == 1) {
            return x;
        }
        if (isPrime(n)) {
            return x;
        } else {
            return y;
        }
    }

    public boolean isPrime(int n) {
        for (int i = 2; i < n; i++) {
            if (n % i == 0) {
                return false;
            }
        }
        return true;
    }
}



