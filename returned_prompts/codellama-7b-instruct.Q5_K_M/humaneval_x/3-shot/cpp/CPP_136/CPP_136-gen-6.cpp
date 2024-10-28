    int smallest_positive = 0;
    int largest_negative = 0;
    for (int i=0;i<lst.size();i++)
    {
        if (lst[i]>0)
        smallest_positive = lst[i];
        if (lst[i]<0)
        largest_negative = lst[i];
    }
    return {largest_negative, smallest_positive};
}


