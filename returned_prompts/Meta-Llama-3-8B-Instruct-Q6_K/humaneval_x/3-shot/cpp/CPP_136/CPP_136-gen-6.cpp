    int max_neg=0, min_pos=INT_MAX;
    for (int i:lst)
    {
        if (i<0)
        {
            if (i>max_neg)
            max_neg=i;
        }
        if (i>0)
        {
            if (i<min_pos)
            min_pos=i;
        }
    }
    if (max_neg<0 && min_pos>0)
    {
        return {max_neg, min_pos};
    }
    else
    {
        return {0, 0};
    }
}