    int i,j,k;
    int sum;
    int size=l.size();
    if (size<3)
    return false;
    for (i=0;i<size;i++)
    for (j=i+1;j<size;j++)
    for (k=j+1;k<size;k++)
    {
        sum=l[i]+l[j]+l[k];
        if (sum==0)
        return true;
    }
    return false;
}


