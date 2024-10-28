        int maxPrimeValue = Integer.MIN_VALUE;
        int sum = 0;

        for (int i = 0; i < lst.size(); i++) {
            if (isPrime(lst.get(i))) {
                int temp = lst.get(i);
                while (temp > 0) {
                    int mod = temp % 10;
                    sum += mod;
                    temp /= 10;
                }

                if (sum > maxPrimeValue) {
                    maxPrimeValue = sum;
                }
                sum = 0;
            }
        }
        return maxPrimeValue;
    }

    public boolean isPrime(int num) {

        if (num <= 1) {
            return false;
        }
        for (int i = 2; i <= Math.sqrt(num); i++) {
            if (num % i == 0) {
                return false;
            }
        }
        return true;
    }

}
































































































































































































































































