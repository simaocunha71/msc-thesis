        int maxPrime = 2;
        for (int i = 0; i < lst.size(); i++) {
            if (isPrime(lst.get(i))) {
                if (lst.get(i) > maxPrime) {
                    maxPrime = lst.get(i);
                }
            }
        }
        return sumDigits(maxPrime);
    }

    public boolean isPrime(int n) {
        if (n <= 1) {
            return false;
        }
        for (int i = 2; i < n; i++) {
            if (n % i == 0) {
                return false;
            }
        }
        return true;
    }

    public int sumDigits(int num) {
        int sum = 0;
        while (num != 0) {
            sum += num % 10;
            num /= 10;
        }
        return sum;
    }
}

