    bool is_sorted = true;
    for (int i=1;i<lst.size();i++)
    if (lst[i-1]>=lst[i])
    {
        is_sorted=false;
    }
    for (int i=1;i<lst.size();i++)
    if (lst[i-1]==lst[i])
    {
        is_sorted=false;
    }
    return is_sorted;
}


