        int max = 0;
        int max_sum = 0;
        for (int i : lst) {
            if (isPrime(i)) {
                if (i > max) {
                    max = i;
                    max_sum = sumDigits(i);
                } else if (i == max && sumDigits(i) > max_sum) {
                    max_sum = sumDigits(i);
                }
            }
        }
        return max_sum;
    }

    private boolean isPrime(int i) {
        if (i == 2) return true;
        if (i % 2 == 0 || i % 3 == 0 || i % 5 == 0) return false;
        for (int j = 6; j * j <= i; j += 6) {
            if (i % (j + 2) == 0) return false;
        }
        return true;
    }

    private int sumDigits(int i) {
        int result = 0;
        while (i > 0) {
            result += i % 10;
            i /= 10;
        }
        return result;
    }
}

