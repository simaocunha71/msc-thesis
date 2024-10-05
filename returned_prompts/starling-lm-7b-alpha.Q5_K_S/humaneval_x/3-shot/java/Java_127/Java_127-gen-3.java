        int start = Math.max(interval1.get(0), interval2.get(0));
        int end = Math.min(interval1.get(1), interval2.get(1));
        int length = end - start + 1;

        if (length <= 0) return "NO";

        if (isPrime(length)) return "YES";
        return "NO";
    }

    private boolean isPrime(int length) {
        if (length < 2) return false;
        if (length == 2) return true;
        if (length % 2 == 0) return false;

        for (int i = 3; i * i <= length; i += 2) {
            if (length % i == 0) return false;
        }
        return true;
    }
}

