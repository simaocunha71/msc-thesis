        if(n <= 2) {
            return 2;
        }
        int a = 2, b = 3;
        int count = 2;
        while(count < n) {
            int temp = a + b;
            a = b;
            b = temp;
            if(isPrime(temp)) {
                count++;
            }
        }
        return b;
    }

    private boolean isPrime(int num) {
        if(num <= 1) {
            return false;
        }
        for(int i = 2; i <= Math.sqrt(num); i++) {
            if(num % i == 0) {
                return false;
            }
        }
        return true;
    }
}