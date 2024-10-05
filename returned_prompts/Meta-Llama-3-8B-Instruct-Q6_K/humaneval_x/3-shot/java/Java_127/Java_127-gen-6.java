        int start1 = Math.max(interval1.get(0), interval2.get(0));
        int end1 = Math.min(interval1.get(1), interval2.get(1));
        if (start1 > end1) return "NO";
        int length = end1 - start1 + 1;
        if (isPrime(length)) return "YES";
        return "NO";
    }

    public boolean isPrime(int n) {
        if (n <= 1) return false;
        if (n == 2) return true;
        if (n % 2 == 0) return false;
        for (int i = 3; i * i <= n; i += 2) {
            if (n % i == 0) return false;
        }
        return true;
    }
}

