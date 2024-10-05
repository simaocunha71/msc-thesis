    int i,j;
    int size=l.size();
    for (i=0;i<size-1;i++)
    for (j=i+1;j<size;j++)
    if (l[i]+l[j]==0)
    return true;

    return false;
}

