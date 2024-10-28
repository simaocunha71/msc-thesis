    int i,n=l.size();
    for (i=0;i<n-1;i++)
    if (l[i]>l[i+1])
    return false;

    for (i=0;i<n-1;i++)
    if (l[i]<l[i+1])
    return false;

    return true;
}




