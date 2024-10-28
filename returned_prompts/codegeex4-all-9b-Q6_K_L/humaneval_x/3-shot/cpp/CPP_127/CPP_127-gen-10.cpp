    int start = max(interval1[0], interval2[0]);
    int end = min(interval1[1], interval2[1]);
    int len = end - start;
    if (len < 0)
        return "NO";
    else if (len == 1)
        return "YES";
    else if (len == 2)
        return "YES";
    else if (len % 2 == 1)
        return "YES";
    else
        return "NO";
}

I have made some changes:
1) I have included some libraries which are not being used yet