        List<Integer> intersection = new ArrayList<>();
        int start = Math.max(interval1.get(0), interval2.get(0));
        int end = Math.min(interval1.get(1), interval2.get(1));
        if (start > end) {
            return "NO";
        }

        for (int i = start; i <= end; i++) {
            intersection.add(i);
        }

        int length = intersection.size();
        return isPrime(length) ? "YES" : "NO";
    }

    public static boolean isPrime(int number) {
        if (number <= 1) {
            return false;
        }
        for (int i = 2; i * i <= number; i++) {
            if (number % i == 0) {
                return false;
            }
        }
        return true;
    }
}


