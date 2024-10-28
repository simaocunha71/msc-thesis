        int start1 = interval1.get(0);
        int end1 = interval1.get(1);
        int start2 = interval2.get(0);
        int end2 = interval2.get(1);

        if (start1 > end2) return "NO";
        if (start2 > end1) return "NO";

        int start = Math.max(start1, start2);
        int end = Math.min(end1, end2);

        int length = end - start + 1;
        if (length <= 0) return "NO";

        if (isPrime(length)) return "YES";
        else return "NO";
    }

    private boolean isPrime(int n) {
        if (n <= 1) return false;
        if (n == 2) return true;
        if (n % 2 == 0) return false;
        for (int i = 3; i * i <= n; i += 2) {
            if (n % i == 0) return false;
        }
        return true;
    }
}

