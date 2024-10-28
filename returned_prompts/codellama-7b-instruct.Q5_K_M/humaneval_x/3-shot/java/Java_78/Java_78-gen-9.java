        int count = 0;
        for (char c : num.toCharArray()) {
            int digit = Character.digit(c, 16);
            if (digit != -1) {
                if (isPrime(digit)) count += 1;
            }
        }
        return count;
    }

    private boolean isPrime(int n) {
        if (n < 2) return false;
        for (int i = 2; i * i <= n; i++) {
            if (n % i == 0) return false;
        }
        return true;
    }
}

