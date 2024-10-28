        int largestPrime = -1;
        for (int i = 0; i < lst.size(); i++) {
            if (isPrime(lst.get(i)) && lst.get(i) > largestPrime) {
                largestPrime = lst.get(i);
            }
        }
        return sumOfDigits(largestPrime);
    }

    private boolean isPrime(int num) {
        if (num <= 1) {
            return false;
        }
        for (int i = 2; i * i <= num; i++) {
            if (num % i == 0) {
                return false;
            }
        }
        return true;
    }

    private int sumOfDigits(int num) {
        int sum = 0;
        while (num > 0) {
            sum += num % 10;
            num /= 10;
        }
        return sum;
    }
}

