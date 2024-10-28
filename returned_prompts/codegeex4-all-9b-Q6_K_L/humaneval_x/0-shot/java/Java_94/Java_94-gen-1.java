public int skjkasdkd(List<Integer> lst) {
        int maxPrime = 0;
        for (int i : lst) {
            if (i > maxPrime && isPrime(i)) {
                maxPrime = i;
            }
        }
        int sum = 0;
        while (maxPrime > 0) {
            sum += maxPrime % 10;
            maxPrime /= 10;
        }
        return sum;
    }

    private boolean isPrime(int n) {
        if (n <= 1) {
            return false;
        }
        for (int i = 2; i <= Math.sqrt(n); i++) {
            if (n % i == 0) {
                return false;
            }
        }
        return true;
    }
}