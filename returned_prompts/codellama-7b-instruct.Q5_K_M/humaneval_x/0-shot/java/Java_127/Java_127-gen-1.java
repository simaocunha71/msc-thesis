        int start1 = interval1.get(0);
        int end1 = interval1.get(1);
        int start2 = interval2.get(0);
        int end2 = interval2.get(1);

        if (start1 > end1 || start2 > end2) {
            return "NO";
        }

        int start = Math.max(start1, start2);
        int end = Math.min(end1, end2);
        if (start > end) {
            return "NO";
        }

        // intersection exists
        int intersectionLength = end - start + 1;
        if (isPrime(intersectionLength)) {
            return "YES";
        }
        return "NO";
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
