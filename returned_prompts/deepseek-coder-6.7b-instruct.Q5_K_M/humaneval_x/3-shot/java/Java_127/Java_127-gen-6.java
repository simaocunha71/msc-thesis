        int start = Math.max(interval1.get(0), interval2.get(0));
        int end = Math.min(interval1.get(1), interval2.get(1));
        int intersection = end - start;

        if (intersection < 2) return "NO";

        for (int i = 2; i * i <= intersection; i++) {
            if (intersection % i == 0) return "NO";
        }
        return "YES";
    }
}

