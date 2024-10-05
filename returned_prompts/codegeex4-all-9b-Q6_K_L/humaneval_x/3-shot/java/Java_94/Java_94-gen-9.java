        int max = 0;

        for (int i : lst) {
            if (i > max && isPrime(i)) max = i;
        }

        int sum = 0;
        while (max > 0) {
            sum += max % 10;
            max /= 10;
        }
        return sum;
    }

    private boolean isPrime(int num) {
        if (num <= 1) return false;
        for (int i = 2; i * i <= num; i++) {
            if (num % i == 0) return false;
        }
        return true;
    }
}

