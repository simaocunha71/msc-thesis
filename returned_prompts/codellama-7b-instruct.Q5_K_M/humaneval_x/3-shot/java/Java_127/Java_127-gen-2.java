        int start1 = interval1.get(0);
        int end1 = interval1.get(1);
        int start2 = interval2.get(0);
        int end2 = interval2.get(1);

        if (end1 < start2 || end2 < start1) {
            return "NO";
        }

        int start = Math.max(start1, start2);
        int end = Math.min(end1, end2);

        int length = end - start + 1;
        if (length <= 0) {
            return "NO";
        }

        if (isPrime(length)) {
            return "YES";
        }

        return "NO";
    }

    private boolean isPrime(int x) {
        if (x == 1 || x == 0) return false;

        for (int i = 2; i < x; i++) {
            if (x % i == 0) {
                return false;
            }
        }

        return true;
    }
}

