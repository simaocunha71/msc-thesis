        int count = 0;
        for (int i = 0; i < num.length(); i++) {
            char c = num.charAt(i);
            if (c == 'A') {
                if (isPrime(2)) count++;
            } else if (c == 'B') {
                if (isPrime(11)) count++;
            } else if (c == 'C') {
                if (isPrime(12)) count++;
            } else if (c == 'D') {
                if (isPrime(13)) count++;
            } else if (c == 'E') {
                if (isPrime(14)) count++;
            } else if (c == 'F') {
                if (isPrime(15)) count++;
            } else {
                count++;
            }
        }
        return count;
    }

    private boolean isPrime(int n) {
        if (n == 1) return false;
        if (n == 2) return true;
        if (n % 2 == 0) return false;
        for (int i = 3; i <= Math.sqrt(n); i += 2) {
            if (n % i == 0) return false;
        }
        return true;
    }
}

