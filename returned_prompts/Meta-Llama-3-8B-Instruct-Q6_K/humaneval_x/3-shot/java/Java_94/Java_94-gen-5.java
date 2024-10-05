        int maxPrime = -1;
        for (int num : lst) {
            if (isPrime(num)) {
                if (num > maxPrime) {
                    maxPrime = num;
                }
            }
        }
        if (maxPrime == -1) {
            return 0;
        }
        int sumOfDigits = 0;
        for (char c : String.valueOf(maxPrime).toCharArray()) {
            sumOfDigits += Character.getNumericValue(c);
        }
        return sumOfDigits;
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