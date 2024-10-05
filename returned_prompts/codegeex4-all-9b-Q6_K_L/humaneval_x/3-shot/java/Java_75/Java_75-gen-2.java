        int count = 0;
        for (int i = 2; i <= a; i++) {
            if (a % i == 0) {
                if (isPrime(i)) count += 1;
            }
        }
        return count == 3;
    }

    private boolean isPrime(int n) {
        for (int i = 2; i <= Math.sqrt(n); i++) {
            if (n % i == 0) return false;
        }
        return true;
    }
}

