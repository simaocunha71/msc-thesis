        int a = 1;
        int b = 2;
        int count = 0;

        while (count < n) {
            int c = a + b;
            a = b;
            b = c;

            if (isPrime(c)) {
                count += 1;
            }
        }
        return a;
    }

    public boolean isPrime(int number) {
        if (number <= 1) return false;
        if (number == 2) return true;
        if (number % 2 == 0) return false;
        for (int i = 3; i <= Math.sqrt(number); i += 2) {
            if (number % i == 0) return false;
        }
        return true;
    }
}

