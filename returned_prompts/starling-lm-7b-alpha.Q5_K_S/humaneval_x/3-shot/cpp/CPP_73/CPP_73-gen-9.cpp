    int i,j;
    int total=0;
    int n=arr.size();
    for (i=0;i<n/2;i++)
    {
        if (arr[i]!=arr[n-i-1])
        {
        total+=1;
        }
    }
    return total;
}


