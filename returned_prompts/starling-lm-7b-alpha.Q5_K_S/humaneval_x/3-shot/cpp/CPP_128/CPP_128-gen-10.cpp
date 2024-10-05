    int i;
    int res=1;
    for (i=0;i<arr.size();i++)
    {
        if (arr[i]==0)
        res*=0;
        if (arr[i]>0)
        res*=1;
        if (arr[i]<0)
        res*=-1;
    }
    return res;
}



