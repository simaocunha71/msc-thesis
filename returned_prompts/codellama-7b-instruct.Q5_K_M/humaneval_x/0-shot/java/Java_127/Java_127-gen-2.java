        int start1 = interval1.get(0);
        int end1 = interval1.get(1);
        int start2 = interval2.get(0);
        int end2 = interval2.get(1);

        if (start1 > end2 || start2 > end1) {
            return "NO";
        }

        int start = Math.max(start1, start2);
        int end = Math.min(end1, end2);

        int length = end - start + 1;

        if (length == 0) {
            return "NO";
        }

        for (int i = 2; i <= length; i++) {
            if (length % i == 0) {
                return "NO";
            }
        }

        return "YES";
    }
}

