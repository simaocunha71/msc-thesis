    int start = max(interval1[0], interval2[0]);
    int end = min(interval1[1], interval2[1]);
    int length = end - start;
    if (length < 0)
        return "NO";
    if (length == 1 || length == 0)
        return "NO";
    for (int i = 2; i * i <= length; i++)
    {
        if (length % i == 0)
        {
            return "NO";
        }
    }
    return "YES";
}


