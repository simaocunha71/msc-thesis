        if (num.length() == 0) return 0;

        int count = 0;
        for (int i = 0; i < num.length(); i++) {
            if (isPrime(num.charAt(i) - 'A' + 2)) count++;
        }

        return count;
    }

    public boolean isPrime(int n) {
        if (n < 2) return false;
        if (n == 2) return true;
        for (int i = 2; i <= Math.sqrt(n); i++) {
            if (n % i == 0) return false;
        }
        return true;
    }
}
