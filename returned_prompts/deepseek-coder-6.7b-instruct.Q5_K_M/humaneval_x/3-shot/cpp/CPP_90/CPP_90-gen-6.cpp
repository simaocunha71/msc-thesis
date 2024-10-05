    int smallest, second_smallest;

    if(lst.size()<2)
        return NULL;

    smallest = second_smallest = INT_MAX;
    for(int i=0; i<lst.size(); i++)
    {
        if(lst[i]<smallest)
        {
            second_smallest = smallest;
            smallest = lst[i];
        }
        else if(lst[i]>smallest && lst[i]<second_smallest)
            second_smallest = lst[i];
    }

    if(second_smallest == INT_MAX)
        return NULL;

    return second_smallest;
}


