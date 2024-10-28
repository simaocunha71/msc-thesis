    if (lst.size()<2)
    return -1;
    sort(lst.begin(),lst.end());
    int second=0;
    for (int i=0;i<lst.size();i++)
    {
        if (i==1)
        return second;
        second=lst[i];
    }
    return -1;
}



