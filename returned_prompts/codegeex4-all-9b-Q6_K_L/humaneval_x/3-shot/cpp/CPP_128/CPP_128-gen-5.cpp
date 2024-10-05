    int sum=0,product=1;
    int i;
    if (arr.size()==0)
    return -32768;
    for (i=0;i<arr.size();i++)
    {
        if (arr[i]==0)
        product=0;
        else if (arr[i]>0)
        product*=1;
        else if (arr[i]<0)
        product*=-1;
        sum+=abs(arr[i]);
    }
    return product*sum;
}

