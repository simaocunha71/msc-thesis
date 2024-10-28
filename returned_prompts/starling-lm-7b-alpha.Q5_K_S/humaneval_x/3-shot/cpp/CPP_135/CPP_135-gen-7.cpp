    int i,n=arr.size(),max_index=-1;
    for (i=0;i<n;i++)
    if (i==0||arr[i]>arr[i-1])
    max_index=i;
    return max_index;
}


