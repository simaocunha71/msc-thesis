        int largest = 1;
        for (int i = 2; i <= n; i++) {
            while (n % i == 0) {
                if (isPrime(i)) largest = i;
                n /= i;
            }
        }
        return largest;
    }

    public boolean isPrime(int n) {
        for (int i = 2; i * i <= n; i++) {
            if (n % i == 0) return false;
        }
        return true;
    }
}

