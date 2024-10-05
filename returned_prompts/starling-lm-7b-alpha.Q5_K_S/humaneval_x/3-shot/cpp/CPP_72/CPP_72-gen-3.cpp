    int i,sum=0;
    int size=q.size();
    for (i=0;i<size;i++)
    sum+=q[i];
    if (sum>w)
    return false;
    if (sum==w)
    return true;
    if (size==1)
    return true;
    for (i=0;i<size/2;i++)
    if (q[i]!=q[size-i-1])
    return false;

    return true;
}



