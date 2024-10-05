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
            }
        }
    }

    public boolean isPrime(int number) {
        if (number <= 1) {
            return false;
        }
        for (int i = 2; i * i <= number; i++) {
            if (number % i == 0) {
                return false;
            }
        }
        return true;
    }
}

