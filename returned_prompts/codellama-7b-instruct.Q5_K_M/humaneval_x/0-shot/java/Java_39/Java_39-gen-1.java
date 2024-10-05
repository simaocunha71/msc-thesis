        int a = 0;
        int b = 1;
        int c = a + b;
        // write your code here
        for (int i = 0; i < n; i++) {
            int temp = c;
            c = a;
            a = b;
            b = temp;
            if (isPrime(c)) {
                return c;
            }
        }
        return -1;
    }

    public boolean isPrime(int n) {
        // write your code here
        if (n == 1) {
            return false;
        }
        if (n == 2) {
            return true;
        }
        if (n % 2 == 0) {
            return false;
        }
        for (int i = 3; i < Math.sqrt(n); i += 2) {
            if (n % i == 0) {
                return false;
            }
        }
        return true;
    }
}

















































































































































































































































































