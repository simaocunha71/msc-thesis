        int result = 0;
        int max_prime = -1;

        for (int i = 0; i < lst.size(); i++) {
            if (isPrime(lst.get(i))) {
                max_prime = Math.max(max_prime, lst.get(i));
            }
        }

        if (max_prime == -1) {
            return result;
        }

        while (max_prime != 0) {
            result += getDigitSum(max_prime % 10);
            max_prime /= 10;
        }

        return result;
    }

    int getDigitSum(int d) {
        return d - (d / 9) * 9;
    }

    boolean isPrime(int n) {
        if (n <= 1) {
            return false;
        }
        if (n <= 3) {
            return true;
        }
        if (n % 2 == 0 || n % 3 == 0) {
            return false;
        }
        for (int i = 5; i * i <= n; i = i + 6) {
            if (n % i == 0 || n % (i + 2) == 0) {
                return false;
            }
        }
        return true;
    }
}

