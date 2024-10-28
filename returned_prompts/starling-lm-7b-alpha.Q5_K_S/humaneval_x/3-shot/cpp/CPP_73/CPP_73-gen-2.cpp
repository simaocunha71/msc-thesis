    int i,j,count=0;
    int n=arr.size();
    int mid=n/2;
    for (i=0;i<mid;i++)
    {
        for (j=n-i-1;j>=mid;j--)
        {
            if (arr[i]!=arr[j])
            {
                count+=1;
            }
        }
    }
    return count;
}



