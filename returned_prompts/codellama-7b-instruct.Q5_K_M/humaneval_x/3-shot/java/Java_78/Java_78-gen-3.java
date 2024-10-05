        int count = 0;
        for (char c : num.toCharArray()) {
            int num_val = 0;
            if (c >= 'A' && c <= 'F') {
                num_val = c - 'A' + 10;
            } else if (c >= '0' && c <= '9') {
                num_val = c - '0';
            }
            if (isPrime(num_val)) {
                count++;
            }
        }
        return count;
    }
    private boolean isPrime(int num) {
        if (num == 2 || num == 3) return true;
        if (num < 2 || num % 2 == 0 || num % 3 == 0) return false;
        int limit = (int) Math.sqrt(num);
        for (int i = 5; i <= limit; i += 6) {
            if (num % i == 0 || num % (i + 2) == 0) {
                return false;
            }
        }
        return true;
    }
}

