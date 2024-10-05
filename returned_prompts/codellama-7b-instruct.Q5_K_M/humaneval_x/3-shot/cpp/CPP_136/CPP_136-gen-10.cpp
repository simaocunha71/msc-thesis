    int largest=0;
    int smallest=0;
    int i;
    for (i=0;i<lst.size();i++)
    {
        if (lst[i]<0)
        {
            if (lst[i]>largest)
            largest=lst[i];
        }
        if (lst[i]>0)
        {
            if (lst[i]<smallest)
            smallest=lst[i];
        }
    }
    vector<int> ret={largest,smallest};
    return ret;
}




