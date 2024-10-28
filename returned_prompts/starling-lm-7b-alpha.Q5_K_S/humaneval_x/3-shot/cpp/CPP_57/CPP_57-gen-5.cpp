    int i;
    int n = l.size();
    for (i=0;i<n-1;i++)
    if (l[i+1]>l[i])
    return false;

    for (i=0;i<n-1;i++)
    if (l[i]<l[i+1])
    return false;
    return true;
}


