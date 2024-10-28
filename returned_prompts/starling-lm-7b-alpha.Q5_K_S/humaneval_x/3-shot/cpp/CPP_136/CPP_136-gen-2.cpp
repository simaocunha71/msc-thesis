    int i,a,b;
    a=b=0;
    for (i=0;i<lst.size();i++)
    {
        if (lst[i]>a && lst[i]<0)
        a=lst[i];
        if (lst[i]>0 && lst[i]<b)
        b=lst[i];
    }
    vector<int> result;
    result.push_back(a);
    result.push_back(b);
    return result;
}




