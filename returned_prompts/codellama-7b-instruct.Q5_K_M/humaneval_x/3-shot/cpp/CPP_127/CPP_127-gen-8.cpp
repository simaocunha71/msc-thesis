    int start1=interval1[0];
    int end1=interval1[1];
    int start2=interval2[0];
    int end2=interval2[1];
    if (end1<start2)
    return "NO";
    if (end2<start1)
    return "NO";
    int start_int=max(start1, start2);
    int end_int=min(end1, end2);
    int length_int=end_int-start_int+1;
    int prime[length_int];
    bool is_prime=false;
    int i;
    for (i=0;i<length_int;i++)
    if (is_prime)
    return "YES";
    return "NO";
}



