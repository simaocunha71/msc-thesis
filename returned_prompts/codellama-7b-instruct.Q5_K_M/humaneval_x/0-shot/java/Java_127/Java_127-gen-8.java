        if (interval1.get(0) > interval2.get(1)) {
            return "NO";
        }
        if (interval1.get(1) < interval2.get(0)) {
            return "NO";
        }
        int start = Math.max(interval1.get(0), interval2.get(0));
        int end = Math.min(interval1.get(1), interval2.get(1));
        int length = end - start;
        for (int i = 2; i <= length; i++) {
            if (length % i == 0) {
                return "NO";
            }
        }
        return "YES";
    }
}
