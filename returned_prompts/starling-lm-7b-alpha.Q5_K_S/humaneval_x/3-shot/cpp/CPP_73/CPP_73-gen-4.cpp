    int i,count=0;
    int n=arr.size();
    for (i=0;i<n;i++)
    {
        if (arr[i]!=arr[n-i-1])
        {
            count+=1;
        }
    }
    return min(count,1+n-count);
}




