    int i,j;
    if (interval1[1]<interval2[0]||interval2[1]<interval1[0])
    return "NO";

    int length=min(interval1[1],interval2[1])-max(interval1[0],interval2[0])+1;

    for (i=2;i<length;i++)
    if (length%i==0)
    return "NO";

    return "YES";
}



