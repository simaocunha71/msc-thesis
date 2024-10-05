    int start,end,start2,end2;
    start=interval1[0];
    end=interval1[1];
    start2=interval2[0];
    end2=interval2[1];
    if (end<start || end2<start2)
    return "NO";
    else
    return (int)abs(end-start+end2-start2)/2>1?"YES":"NO";
}


