        int a = 0, b = 1, count = 0;
        while (count < n) {
            int temp = a + b;
            a = b;
            b = temp;
            if (isPrime(b)) {
                count++;
            }
        }
        return b;
    }

    public boolean isPrime(int n) {
        if (n <= 1) return false;
        for (int i = 2; i * i <= n; i++) {
            if (n % i == 0) return false;
        }
        return true;
    }
}

