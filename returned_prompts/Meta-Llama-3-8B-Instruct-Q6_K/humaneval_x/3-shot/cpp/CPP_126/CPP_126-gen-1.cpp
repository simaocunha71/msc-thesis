    bool sorted=true;
    int i;
    for (i=1;i<lst.size();i++)
    {
        if (lst[i-1]>lst[i])
        {
            sorted=false;
            break;
        }
        if (lst[i-1]==lst[i])
        {
            sorted=false;
            break;
        }
    }
    return sorted;
}