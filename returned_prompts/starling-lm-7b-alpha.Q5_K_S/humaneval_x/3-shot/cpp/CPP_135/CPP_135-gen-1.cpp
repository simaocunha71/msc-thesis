    int i,n=arr.size();
    for (i=0;i<n-1;i++)
    if (arr[i]<arr[i+1])
    return i;
    return -1;
}

