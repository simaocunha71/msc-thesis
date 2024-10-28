        int intersection_start = Math.max(interval1.get(0), interval2.get(0));
        int intersection_end = Math.min(interval1.get(1), interval2.get(1));

        int intersection_length = intersection_end - intersection_start;

        if (intersection_length < 2) return "NO";

        for (int i = 2; i < intersection_length; i++) {
            if (intersection_length % i == 0) return "NO";
        }

        return "YES";
    }
}

