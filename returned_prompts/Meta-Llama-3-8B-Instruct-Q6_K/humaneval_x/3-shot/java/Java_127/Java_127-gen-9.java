        int start = Math.max(interval1.get(0), interval2.get(0));
        int end = Math.min(interval1.get(1), interval2.get(1));

        if (start > end) {
            return "NO";
        }

        int intersectionLength = end - start + 1;
        if (isPrime(intersectionLength)) {
            return "YES";
        } else {
            return "NO";
        }
    }

    public boolean isPrime(int num) {
        if (num <= 1) {
            return false;
        }
        for (int i = 2; i * i <= num; i++) {
            if (num % i == 0) {
                return false;
            }
        }
        return true;
    }
}

