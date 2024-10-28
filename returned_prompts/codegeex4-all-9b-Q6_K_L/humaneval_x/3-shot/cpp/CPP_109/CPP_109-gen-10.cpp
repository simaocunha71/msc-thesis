    int i,j;
    int k=0;
    int l=0;
    for (i=0;i<arr.size();i++)
    {
        if (arr[i]>arr[i+1])
        {
            k=1;
        }
        if (k==1&&arr[i]<arr[i+1])
        {
            l=1;
        }
    }
    if (l==1)
    return false;
    else
    return true;

}

