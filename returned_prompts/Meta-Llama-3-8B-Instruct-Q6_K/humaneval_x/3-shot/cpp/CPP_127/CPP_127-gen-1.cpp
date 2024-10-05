    int start = max(interval1[0], interval2[0]);
    int end = min(interval1[1], interval2[1]);
    if (start > end) {
        return "NO";
    }
    int intersection_length = end - start + 1;
    if (intersection_length <= 1) {
        return "NO";
    }
    int i = 2;
    while (i * i <= intersection_length) {
        if (intersection_length % i == 0) {
            return "NO";
        }
        i++;
    }
    return "YES";
}

