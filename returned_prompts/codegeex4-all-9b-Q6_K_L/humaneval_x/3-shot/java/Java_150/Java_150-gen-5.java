        if (isPrime(n)) return x;
        return y;
    }

    private boolean isPrime(int n) {
        if (n < 2) return false;
        for (int i = 2; i < Math.sqrt(n); i++) {
            if (n % i == 0) return false;
        }
        return true;
    }
}

