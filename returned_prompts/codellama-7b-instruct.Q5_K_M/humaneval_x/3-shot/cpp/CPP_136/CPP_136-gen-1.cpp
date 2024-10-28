    int largest_negative=0;
    int smallest_positive=0;
    int i;
    for (i=0;i<lst.size();i++)
    if (lst[i]<0){
        if (lst[i]>largest_negative)
        largest_negative=lst[i];
        }
    for (i=0;i<lst.size();i++)
    if (lst[i]>0){
        if (lst[i]<smallest_positive)
        smallest_positive=lst[i];
        }
    return {largest_negative,smallest_positive};
}


