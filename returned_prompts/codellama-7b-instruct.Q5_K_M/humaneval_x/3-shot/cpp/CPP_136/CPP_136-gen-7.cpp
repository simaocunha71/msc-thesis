    int largest_negative_int=0;
    int smallest_positive_int=0;
    for (int i=0;i<lst.size();i++)
    {
        if (lst[i]<0)
        {
            if (lst[i]<largest_negative_int)
            largest_negative_int=lst[i];
        }
        if (lst[i]>0)
        {
            if (lst[i]>smallest_positive_int)
            smallest_positive_int=lst[i];
        }
    }
    return {largest_negative_int, smallest_positive_int};
}


