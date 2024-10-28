    int start,end,start2,end2;
    start=interval1[0];
    end=interval1[1];
    start2=interval2[0];
    end2=interval2[1];

    if(end<start2 || start>end2)
        return "NO";

    int intersection_start=max(start,start2);
    int intersection_end=min(end,end2);

    int intersection_length=intersection_end-intersection_start+1;

    if(intersection_length<2)
        return "NO";

    for(int i=2; i*i<=intersection_length; ++i)
    {
        if(intersection_length % i == 0)
            return "NO";
    }

    return "YES";
}


