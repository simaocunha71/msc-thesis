    int i,j,k;
    int size=l.size();
    for (i=0;i<size-2;i++)
    for (j=i+1;j<size-1;j++)
    for (k=j+1;k<size;k++)
    if (l[i]+l[j]+l[k]==0)
    return true;

    return false;
}

