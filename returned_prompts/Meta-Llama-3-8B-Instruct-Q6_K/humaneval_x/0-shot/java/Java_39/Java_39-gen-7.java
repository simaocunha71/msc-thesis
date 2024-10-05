        int a = 1, b = 1;
        int count = 1;
        while (true) {
            if (isPrime(b)) {
                if (count == n) {
                    return b;
                }
                count++;
            }
            a = a + b;
            b = a - b;
        }
    }

    boolean isPrime(int num) {
        if (num <= 1) {
            return false;
        }
        for (int i = 2; i <= Math.sqrt(num); i++) {
            if (num % i == 0) {
                return false;
            }
        }
        return true;
    }
}

