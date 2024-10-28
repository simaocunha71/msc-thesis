        int start1 = interval1.get(0);
        int end1 = interval1.get(1);
        int start2 = interval2.get(0);
        int end2 = interval2.get(1);

        if (start1 > end2 || start2 > end1) return "NO";

        int intersection_start = Math.max(start1, start2);
        int intersection_end = Math.min(end1, end2);

        int intersection_length = intersection_end - intersection_start + 1;

        if (intersection_length <= 1) return "NO";

        boolean is_prime = false;
        for (int i = 2; i < intersection_length; i++) {
            if (intersection_length % i == 0) break;
            else if (i == intersection_length - 1) is_prime = true;
        }

        if (is_prime) return "YES";
        else return "NO";

    }
}

