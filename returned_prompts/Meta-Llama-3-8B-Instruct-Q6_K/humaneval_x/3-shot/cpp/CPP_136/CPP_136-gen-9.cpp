    int largest_negative=INT_MIN, smallest_positive=INT_MAX;
    for (int i : lst)
    {
        if (i<0 && i>largest_negative)
        largest_negative=i;
        if (i>0 && i<smallest_positive)
        smallest_positive=i;
    }
    if (largest_negative==INT_MIN)
    largest_negative=0;
    if (smallest_positive==INT_MAX)
    smallest_positive=0;
    return {largest_negative, smallest_positive};
}