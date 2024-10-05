    public String intersection(List<Integer> interval1, List<Integer> interval2) {
        int start1 = Math.max(interval1.get(0), interval2.get(0));
        int end1 = Math.min(interval1.get(1), interval2.get(1));
        if (start1 > end1) {
            return "NO";
        }

        int intersectionLength = end1 - start1 + 1;
        if (isPrime(intersectionLength)) {
            return "YES";
        } else {
            return "NO";
        }
    }

    public boolean isPrime(int n) {
        if (n <= 1) {
            return false;
        }
        for (int i = 2; i * i <= n; i++) {
            if (n % i == 0) {
                return false;
            }
        }
        return true;
    }