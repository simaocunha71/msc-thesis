        int number = a;
        for (int i = 2; i < number; i++) {
            if (number % i == 0) {
                while (number % i == 0) {
                    number /= i;
                }
                if (!isPrime(i)) return false;
            }
        }
        return isPrime(number);
    }

    public boolean isPrime(int number) {
        for (int i = 2; i <= Math.sqrt(number); i++) {
            if (number % i == 0) return false;
        }
        return true;
    }
}

