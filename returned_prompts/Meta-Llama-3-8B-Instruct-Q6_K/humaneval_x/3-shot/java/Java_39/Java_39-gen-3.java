        int a = 0, b = 1, count = 0;
        while (count < n) {
            int temp = a + b;
            if (isPrime(temp)) {
                a = b;
                b = temp;
                count++;
            } else {
                a = a + b;
            }
        }
        return b;
    }

    public boolean isPrime(int num) {
        if (num <= 1) return false;
        for (int i = 2; i * i <= num; i++) {
            if (num % i == 0) return false;
        }
        return true;
    }
}

