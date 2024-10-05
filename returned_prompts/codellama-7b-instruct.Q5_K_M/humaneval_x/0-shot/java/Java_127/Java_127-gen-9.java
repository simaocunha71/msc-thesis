        int start1 = interval1.get(0);
        int end1 = interval1.get(1);

        int start2 = interval2.get(0);
        int end2 = interval2.get(1);

        if (start1 <= end2 && start2 <= end1) {
            int intersectionStart = Math.max(start1, start2);
            int intersectionEnd = Math.min(end1, end2);
            int intersectionLength = intersectionEnd - intersectionStart + 1;

            if (intersectionLength == 1) {
                return "NO";
            }

            if (isPrime(intersectionLength)) {
                return "YES";
            } else {
                return "NO";
            }
        }
        return "NO";
    }

    public boolean isPrime(int n) {
        if (n <= 1) return false;
        for (int i = 2; i <= (int) Math.sqrt(n); i++) {
            if (n % i == 0) return false;
        }
        return true;
    }
}
