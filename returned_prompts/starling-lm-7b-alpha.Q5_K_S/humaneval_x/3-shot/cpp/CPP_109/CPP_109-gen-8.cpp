    int i,n=arr.size();
    if (n==0)
    return true;
    if (n==1)
    return true;
    if (n==2)
    {
        if (arr[0]<arr[1])
        return true;
        else
        return false;
    }
    int max=arr[0],max_ind=0;
    for (i=1;i<n;i++)
    if (arr[i]>max){
        max=arr[i];
        max_ind=i;
    }
    if (max_ind==(n-1))
    return true;
    else
    return false;
}


