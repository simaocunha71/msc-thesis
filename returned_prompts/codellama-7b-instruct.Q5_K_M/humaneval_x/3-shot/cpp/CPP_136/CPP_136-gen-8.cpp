    int a=0,b=0;
    int i;
    for (i=0;i<lst.size();i++)
    {
        if (lst[i]>0 && lst[i]>b)
        b=lst[i];
        if (lst[i]<0 && lst[i]<a)
        a=lst[i];
    }
    return vector<int>{a,b};
}

