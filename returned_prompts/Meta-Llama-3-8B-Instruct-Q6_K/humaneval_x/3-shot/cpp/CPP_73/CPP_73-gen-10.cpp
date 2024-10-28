    int i;
    int res=0;
    for (i=0;i<arr.size();i++)
    {
        if (arr[i]!=arr[arr.size()-i-1])
        res++;
    }
    return res;
}