    if (interval1[0]>=interval2[1] || interval1[1]<=interval2[0])
    return "NO";
    int start=max(interval1[0],interval2[0]);
    int end=min(interval1[1],interval2[1]);
    return "YES";
}


