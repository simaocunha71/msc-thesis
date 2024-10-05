        int a = 0, b = 1;
        int count = 0;
        while (true) {
            int temp = a + b;
            if (isPrime(temp)) {
                a = b;
                b = temp;
                count++;
                if (count == n) {
                    return b;
                }
            } else {
                a = a + b;
            }
        }
    }

    public boolean isPrime(int n) {
        if (n < 2) {
            return false;
        }
        for (int i = 2; i <= Math.sqrt(n); i++) {
            if (n % i == 0) {
                return false;
            }
        }
        return true;
    }
}

