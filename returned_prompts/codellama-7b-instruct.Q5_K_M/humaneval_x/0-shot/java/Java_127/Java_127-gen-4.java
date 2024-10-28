        if (interval1 == null || interval2 == null) {
            return "NO";
        }

        if (interval1.size() != 2 || interval2.size() != 2) {
            return "NO";
        }

        if (interval1.get(0) > interval2.get(1) || interval1.get(1) < interval2.get(0)) {
            return "NO";
        }

        int start = Math.max(interval1.get(0), interval2.get(0));
        int end = Math.min(interval1.get(1), interval2.get(1));

        if (end < start) {
            return "NO";
        }

        return isPrime(end - start) ? "YES" : "NO";
    }

    private boolean isPrime(int n) {
        if (n < 2) {
            return false;
        }

        for (int i = 2; i * i <= n; i++) {
            if (n % i == 0) {
                return false;
            }
        }

        return true;
    }
}
