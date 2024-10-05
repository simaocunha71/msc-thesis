        int start1 = interval1.get(0);
        int end1 = interval1.get(1);
        int start2 = interval2.get(0);
        int end2 = interval2.get(1);

        int intersection_start = Math.max(start1, start2);
        int intersection_end = Math.min(end1, end2);

        if (intersection_start <= intersection_end) {
            int length = intersection_end - intersection_start + 1;
            if (length == 1) {
                return "NO";
            } else if (isPrime(length)) {
                return "YES";
            } else {
                return "NO";
            }
        } else {
            return "NO";
        }
    }

    private boolean isPrime(int number) {
        if (number <= 1) {
            return false;
        }
        for (int i = 2; i < number; i++) {
            if (number % i == 0) {
                return false;
            }
        }
        return true;
    }
}

