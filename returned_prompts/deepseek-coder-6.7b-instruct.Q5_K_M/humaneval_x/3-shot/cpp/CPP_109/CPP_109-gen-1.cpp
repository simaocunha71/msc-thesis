    int n=arr.size();
    if(n==0)
    return true;
    for(int i=0; i<n-1; i++)
    {
        if(arr[i]>arr[i+1])
        return false;
    }
    if(arr[n-1]>arr[0])
    return false;
    return true;
}

