        int start1 = interval1.get(0);
        int end1 = interval1.get(1);
        int start2 = interval2.get(0);
        int end2 = interval2.get(1);

        if (end1 < start2 || end2 < start1) return "NO";

        int start = Math.max(start1, start2);
        int end = Math.min(end1, end2);

        if (end <= start) return "NO";

        int length = end - start;

        boolean isPrime = true;
        for (int i = 2; i <= Math.sqrt(length); i++) {
            if (length % i == 0) {
                isPrime = false;
                break;
            }
        }

        if (isPrime) return "YES";

        return "NO";
    }
}

