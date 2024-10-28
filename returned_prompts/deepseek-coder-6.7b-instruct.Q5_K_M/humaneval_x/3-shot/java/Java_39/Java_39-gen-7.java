        int count = 0;
        int i = 2;
        while (count < n) {
            if (isPrime(i) && isFibonacci(i)) {
                count++;
            }
            i++;
        }
        return i - 1;
    }

    private boolean isPrime(int n) {
        if (n <= 1) {
            return false;
        }
        for (int i = 2; i * i <= n; i++) {
            if (n % i == 0) {
                return false;
            }
        }
        return true;
    }

    private boolean isFibonacci(int n) {
        int a = 0;
        int b = 1;
        while (b < n) {
            int temp = b;
            b = a + b;
            a = temp;
        }
        return b == n;
    }
}

