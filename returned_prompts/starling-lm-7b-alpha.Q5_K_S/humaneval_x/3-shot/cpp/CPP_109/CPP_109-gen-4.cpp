    int i,n;
    n=arr.size();
    for (i=0;i<n-1;i++)
    if (arr[i+1]<arr[i])
    return false;
    return true;
}


