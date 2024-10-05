    int i,res;
    res=1;
    for (i=0;i<arr.size();i++)
    {
        if (arr[i]==0)
        res*=0;
        if (arr[i]==1)
        res*=1;
        if (arr[i]==-1)
        res*=-1;
    }
    return res;
}

