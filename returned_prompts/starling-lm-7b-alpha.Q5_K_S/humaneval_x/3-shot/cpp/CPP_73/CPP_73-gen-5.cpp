    int i,j,n=arr.size();
    int count=0;
    for (i=0;i<n;i++)
    for (j=0;j<n;j++)
    if (i<j && arr[i]!=arr[j])
    count+=1;

    return n-1-count/2;
}




