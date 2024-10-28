    public int skjkasdkd(List<Integer> lst) {
        int maxPrime = 0;
        for (int num : lst) {
            if (isPrime(num) && num > maxPrime) {
                maxPrime = num;
            }
        }
        if (maxPrime == 0) {
            return 0;
        }
        int sumOfDigits = 0;
        while (maxPrime > 0) {
            sumOfDigits += maxPrime % 10;
            maxPrime /= 10;
        }
        return sumOfDigits;
    }

    public boolean isPrime(int num) {
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
}
