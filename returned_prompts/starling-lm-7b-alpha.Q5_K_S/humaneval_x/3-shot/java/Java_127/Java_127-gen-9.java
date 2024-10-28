        int start = Math.max(interval1.get(0), interval2.get(0));
        int end = Math.min(interval1.get(1), interval2.get(1));
        int intersection_length = end - start + 1;

        if (intersection_length == 0) return "NO";
        if (intersection_length == 1) return "NO";

        boolean is_prime = true;
        for (int i = 2; i <= Math.sqrt(intersection_length); i++) {
            if (intersection_length % i == 0) {
                is_prime = false;
                break;
            }
        }
        return is_prime ? "YES" : "NO";
    }
}

