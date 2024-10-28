    if (lst.size()<2)
        return 0;
    sort(lst.begin(),lst.end());
    int i;
    for (i=0;i<lst.size()-1;i++)
        if (lst[i]!=lst[i+1])
            return lst[i+1];
    return 0;
}

