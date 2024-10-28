    int i;
    if (arr.size()==0)
    return -32768;
    int sum=0;
    int prod=1;
    for (i=0;i<arr.size();i++)
    {
        sum+=abs(arr[i]);
        prod*=arr[i];
    }
    return sum*prod;
}

