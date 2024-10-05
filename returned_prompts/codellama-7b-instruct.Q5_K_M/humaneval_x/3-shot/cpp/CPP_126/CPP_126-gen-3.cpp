    bool is_sorted=true;
    int i;
    int prev=0;
    for (i=0;i<lst.size();i++)
    {
        if (lst[i]<prev)
        {
            is_sorted=false;
        }
        if (lst[i]==prev)
        {
            is_sorted=false;
        }
        prev=lst[i];
    }
    return is_sorted;
}


