    if(arr.size()==0)
    return -32768;
    int prod=1;
    int sum=0;
    for(int i=0;i<arr.size();i++)
    {
        if(arr[i]<0)
        prod*=-1;
        if(arr[i]>0)
        prod*=1;
        if(arr[i]==0)
        return 0;
        sum+=abs(arr[i]);
    }
    return prod*sum;
}


