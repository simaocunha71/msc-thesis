    int max_neg=INT_MIN;
    int min_pos=INT_MAX;
    for (int i:lst)
    {
        if (i<0 && i>max_neg)
        max_neg=i;
        if (i>0 && i<min_pos)
        min_pos=i;
    }
    return {(max_neg<0)?max_neg:0, (min_pos!=INT_MAX)?min_pos:0};
}